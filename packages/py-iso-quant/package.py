# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIsoQuant(PythonPackage):
    """Reference-based analysis and quantification of long RNA reads."""

    homepage = "https://github.com/ablab/IsoQuant"
    url = "https://github.com/ablab/IsoQuant/releases/download/v3.12.2/IsoQuant-3.12.2.tar.gz"

    license("GPL-2.0-only")

    version("3.12.2", sha256="184d1970694536a24f9214095908fef6b22743a0f8722784adcecd06969d5e8f")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@64:", type="build")

    depends_on("py-gffutils@0.10.1:", type=("build", "run"))
    depends_on("py-pandas@1.0.1:", type=("build", "run"))
    depends_on("py-pysam@0.15:", type=("build", "run"))
    depends_on("py-pyfaidx@0.7:", type=("build", "run"))
    depends_on("py-ssw-py@1.0.0:", type=("build", "run"))
    depends_on("py-pyyaml@5.4:", type=("build", "run"))
    depends_on("py-matplotlib@3.1.3:", type=("build", "run"))
    depends_on("py-numpy@1.24:", type=("build", "run"))
    depends_on("py-scipy@1.10:", type=("build", "run"))
    depends_on("py-seaborn@0.10:", type=("build", "run"))
    depends_on("py-editdistance@0.8.1:", type=("build", "run"))
    depends_on("py-biopython@1.76:", type=("build", "run"))
    depends_on("py-numba@0.58:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            isoquant = Executable(join_path(self.prefix.bin, "isoquant"))
            isoquant("--help")
