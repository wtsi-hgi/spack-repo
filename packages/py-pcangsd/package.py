# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPcangsd(PythonPackage):
    """Framework for analyzing low depth NGS data in heterogeneous populations using PCA"""
    
    homepage = "https://github.com/Rosemeis/pcangsd"
    pypi = "pcangsd/pcangsd-1.36.4.tar.gz" 

    version("1.36.0", sha256="54700832b72eddd88beb1dd318a62b1b8304b6ca0836969085e58042877ba51d")
    version("1.36.1", sha256="80d6ba59ba1d1d04daa0aeeff1bb27a04e40442771ec9031ca463fb5af7c6ef4")
    version("1.36.2", sha256="dd04d3a2eb6d54bff3eb6cc3a62b98ee342591399b99fa513d0308e78c6fce20")
    version("1.36.3", sha256="678be169890b917cd762a77d70a23014d39ddf9da69028543aa1c23189576549")
    version("1.36.4", sha256="7313a43b2af2d57635fc48ddb8fe59cb6ff99e647ffe7fe977d5597c70bf5ac9")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        """Exercise the main executable after installing."""
        pcangsd = Executable(join_path(self.prefix.bin, "pcangsd"))
        with working_dir("spack-test", create=True):
            pcangsd("--help")