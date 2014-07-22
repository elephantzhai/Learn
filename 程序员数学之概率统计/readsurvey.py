import survey
import Pmf
import Cdf

def _MakeTables(data_dir='.'):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    first,others = PartitionRecodes(table)

    return table,first,others

def PartitionRecodes(table):
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for p in table.records:
        if p.outcome !=1:
            continue

        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)

    return firsts,others

def PoolRecords(*tables):
    pool = survey.Pregnancies()
    for table in tables:
        pool.ExtendRecords(table.records)
    return pool

def ProcessLength(table):
    table.lengths = [p.prglength for p in table.records]

def ProcessWeight(table):
    table.weights = [p.totalwgt_oz for p in table.records if p.totalwgt_oz !='NA']

def Process(table):
    processes = [ProcessLength,ProcessWeight]
    for process in processes:
        process(table)

def Processs(*tables):
    for table in tables:
        Process(table)

def MakeTables():
    table,firsts,others = _MakeTables()
    pool = PoolRecords(firsts,others)

    Processs(pool,firsts,others)

    return pool,firsts,others





def Test():
    MakeTables()

if __name__ == '__main__':
    Test()