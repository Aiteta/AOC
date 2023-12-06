#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>

bool isLower(const std::string& val) {
    if (val == "end" || val == "start")
        return false;
    if (val[0] >= 'a' && val[0] <= 'z')
        return true;
    return false;
}

int explore(std::map<std::string, std::vector<std::string> >& graph, std::set<std::string> visited, const std::string& cur, bool second) {
    if (cur == "end") 
        return 1;
    if (isLower(cur))
        visited.insert(cur);
    int out = 0;
    auto vec = graph[cur];
    for (auto itr : graph[cur]) {
        if (itr == "start")
            continue;
        if (visited.count(itr) && !second)
            out += explore(graph,visited,itr,true);
        else if (visited.count(itr) && second)
            continue;
        else
            out += explore(graph,visited,itr,second);
    }
    return out;
}

void build_graph(std::map<std::string, std::vector<std::string> >& graph) {
    std::ifstream f("input12.txt");
    std::string input;
    std::string w1;
    std::string w2;
    int i;
    while (f >> input) {
        for (i = 0; input[i] != '-'; i++) {}
        w1 = input.substr(0,i);
        w2 = input.substr(i+1,input.size());
        graph[w1].push_back(w2);
        graph[w2].push_back(w1);
    }
}

int main() {
    std::map<std::string, std::vector<std::string> > graph;
    build_graph(graph);
    std::cout << explore(graph,std::set<std::string>(), "start",false) << std::endl;
    return 0;
}