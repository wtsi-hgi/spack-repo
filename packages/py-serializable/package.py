# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySerializable(PythonPackage):
    """Base class with serialization helpers for user-defined Python objects"""

    homepage = "https://github.com/iskandr/serializable"
    pypi = "serializable/serializable-0.4.1-py3-none-any.whl"

    version("0.0.1", sha256="a5c0d5d5d3e6f47fddc6a7e1de6e34e16d19893e5714c0ea43dfe4208993aecf")
    version("0.0.2", sha256="1f5b6aab7fd133093fac53b9dca27fad50e175c5d50f72f2227dea3020b32205")
    version("0.0.4", sha256="92a7ae43184ce538847519acf9bbcdc0e2a7d35c8adfba4f83c24156b06dc467")
    version("0.0.5", sha256="d0cf7bd964da19eb1a182d0394016a1a0c7ef004b6b5a1059d86811f4959a273")
    version("0.0.6", sha256="20d2f748f92d835829db112eacb820814e3155f3069610d300fcbf806ea456ee")
    version("0.0.7", sha256="0d02855c7023c8409fac7fb16aef9ee71f4a911e77f96044da910d803967b3e2")
    version("0.0.8", sha256="fa35fb672e9d8148832faae7e6a27e1a851a1a09054515cb081ec22cfa9e1c78")
    version("0.0.9", sha256="c9f21aea5b8ad5704f46dc67f0c0e4167d599f3a5c276df6f127f2eea9b42bee")
    version("0.1.0", sha256="a2a2c335e68ce2f5c2397a726b67c8da74f86fcef3cdbff2223b4d639583401c")
    version("0.1.1", sha256="87f9fadbd0fba5c7951858d16ae9109afa4c96fd486e663419f3051f352a22d9")
    version("0.2.0", sha256="2b93a876aa0b9945235aec9bdd554707d44b39e878695a9b0d9af8acc2e02f87")
    version("0.2.1", sha256="ec604e5df0c1236c06d190043a407495c4412dd6b6fd3b45a8514518173ed961")
    version("0.3.0", sha256="fa172474e57437fffab01a01444661f7577bf88aa802313e705afcf0bdbfce53", expand=False, url="https://files.pythonhosted.org/packages/de/8f/ab51fbeacbd3fcc527032b4e99139370dc5ce09c734a83dfb9be51d78479/serializable-0.3.0-py3-none-any.whl")
    version("0.4.0", sha256="ce756a8e9a2e1ccee4c1ddbb4f33a677c4132c68220abd79ed7db4b56c9b787c", expand=False, url="https://files.pythonhosted.org/packages/ee/1d/fc08c06ffde841414a02799d70ccee2c0f3cfed48ef1df3495b7889f7017/serializable-0.4.0-py3-none-any.whl")
    version("0.4.1", sha256="d1f09fade42cc49f9cdf138cd8d2d3515beb1605507ae26983ea812bae77b3e2", expand=False, url="https://files.pythonhosted.org/packages/bd/a6/736a99c39baa85cf51922526525300fb732f2d31138c28ae1634370bf8bf/serializable-0.4.1-py3-none-any.whl")

    depends_on("py-setuptools", type="build")
    depends_on("py-typechecks", type=("build", "run"))
    depends_on("py-simplejson", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import serializable")

# {'typechecks>=0.0.2': ['0.3.0', '0.4.0', '0.4.1'], 'simplejson': ['0.3.0', '0.4.0', '0.4.1']}
