say Hi Tempest Plugin
=========

Having simple say hi python package.

Add integration test cases compatible with OpenStack Tempest tool by implementing Tempest Plugin into our package.

Plugin implementation will allow to run package integration test cases via testr test runner and tempest suite.

Package Structure

.. code-block:: bash

  say_hi_tempest_plugin
  ├── demo                              ──┐
  │   ├── __init__.py                     │
  │   ├── src                             │
  │   │   ├── __init__.py                 │── Simple say_hi package structure
  │   │   ├── say_hi.py                   │ 
  │   └── tests                           │
  │       ├── __init__.py                 │
  │       └── test_sayhi.py             ──┘
  ├── demo_tempest_plugin
  │   ├── config.py                     <─ Configuration Options to be register
  │   ├── __init__.py
  │   ├── plugin.py                     <─ Actual tempest plugin, Registration method of options and groups
  │   └── tests                         <─ Integration Test Cases for the program
  │       ├── api                       ──┐
  │       │   ├── base.py                 │
  │       │   ├── __init__.py             │── Integration Test Cases(optional structure)
  │       │   └── test_int_sayhi.py       │
  │       ├── scenario                    │
  │       └── __init__.py               ──┘ 
  ├── LICENSE
  ├── README.rst
  ├── requirements.txt
  └── setup.py                          <─ Added Tempest entry point

Installation
----

To install Tempest

.. code-block:: bash

  $ git clone https://github.com/openstack/tempest/
  $ pip install tempest/

To install say hi plugin

.. code-block:: bash

  $ git clone https://github.com/dlux/sayHi_tempest_plugin.git
  $ pip install sayHi_tempest_plugin/

Initialize Tempest

.. code-block:: bash

  # Initialize Tempest
  $ cd tempest
  $ testr init

Run Test Suite
------

Validate Temepst discovered the TCs

.. code-block:: bash

  $ testr list-tests | grep -i say

  2016-03-21 18:08:17.242 5732 INFO tempest [-] Using tempest config file
  /etc/tempest/tempest.conf 
  demo_tempest_plugin.tests.api.test_int_sayhi.TestSayHiInt.test_hi[smoke]

Run test cases

.. code-block:: bash

  $ testr run demo_tempest_plugin.tests.api.test_int_sayhi.TestSayHiInt.test_hi

.. code-block:: bash

  $ testr run --subunit smoke | subunit-1to2 | subunit-trace --color -n

.. code-block:: bash

  $ ./tempest/run_tempest.sh demo_tempest_plugin.tests.api.test_int_sayhi.TestSayHiInt.test_hi -N

Other Resources
------

Run say hi program

.. code-block:: bash

  $ dluxsay
  Hello Stranger

  # with parameters
  $ dluxsay Luz
  Hi Luz

Resources

http://docs.openstack.org/developer/tempest/plugin.html

http://docs.openstack.org/developer/oslo.config/cfg.html

http://specs.openstack.org/openstack/qa-specs/specs/tempest/tempest-external-plugin-interface.html
