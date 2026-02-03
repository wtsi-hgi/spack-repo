# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCellregulondb(PythonPackage):
    """Python package for downloading and analysing data from the CellRegulon database."""
    
    homepage = "https://github.com/Teichlab/cellregulondb"
    pypi = "cellregulondb/cellregulondb-0.1.0-py3-none-any.whl" 

    version("0.1.0", sha256="ab30550ba1df1c870ddd6540193e514489595b7efb1b6ee585558ea38c8653c0", expand=False, url="https://files.pythonhosted.org/packages/5d/d3/9cb0baa560ca433c9958c726012df0adddf0ea64e55e0ba4382a0b213983/cellregulondb-0.1.0-py3-none-any.whl")

    license("MIT")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import cellregulondb")

# {'pandas': ['0.1.0'], 'requests': ['0.1.0'], 'rich': ['0.1.0'], 'networkx': ['0.1.0']}