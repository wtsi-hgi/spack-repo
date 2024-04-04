# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyVmd(PythonPackage):
    """Installable VMD as a python module"""

    homepage = "https://github.com/Eigenstate/vmd-python"
    git = "https://github.com/Eigenstate/vmd-python"

    version("3.1.4", tag="v3.1.4")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))

    depends_on("netcdf-c", type=("build", "link", "run"))
    depends_on("expat", type=("build", "link", "run"))
    depends_on("sqlite", type=("build", "link", "run"))
    depends_on("tcl-tcllib", type=("build", "link", "run"))
    depends_on("tcl", type=("build", "link", "run"))
    depends_on("tk", type=("build", "link", "run"))
    depends_on("py-importlib-resources", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        env.set("LD_LIBRARY_PATH", self.spec["tcl"].prefix.lib + ":" + 
                                   self.spec["sqlite"].prefix.lib + ":" +
                                   self.spec["expat"].prefix.lib + ":" +
                                   self.spec["netcdf-c"].prefix.lib)
