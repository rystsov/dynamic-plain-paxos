# Dynamic Plain Paxos

## Abstract

The classic Paxos consensus algorithm requires a static set of 2F + 1 processes to tolerate F transient failures. Dynamic Plain Paxos is an extension and a drop-in replacement for the classic Paxos algorithm that allows to change the membership during the reaching of consensus. It satisfies the requirements of the real world systems to replace a permanently failed node or to extend the size of the cluster to tolerate more transient failures.

The article describes a generic way to prove the correctness of paxos-based distributes systems during the change of configuration and uses it to prove the correctness of membership changes.

Url: [http://rystsov.info/files/dynamic-plain-paxos.pdf](http://rystsov.info/files/dynamic-plain-paxos.pdf)