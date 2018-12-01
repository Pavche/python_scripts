# coding: utf-8
# Prerequisites
# 1. Install Nitrate API.
#
# Example https://github.com/psss/python-nitrate/blob/master/examples/create.py
import nitrate

tcms_plan_id = 24500
test_list = []

f = open('tests.txt', 'r')
for line in f.readlines():
    test_list.append(line.strip())

# Remove the last empty element.
test_list.pop()

plan = nitrate.TestPlan(tcms_plan_id)
for t in tests:
    testcase = nitrate.TestCase(summary="%s" % t, product="Red Hat Enterprise Linux 7", category="Sanity", script="testname=%s" % t)
    plan.testcases.add(testcase)
    plan.update()
