# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCbgen(PythonPackage):
    """BGEN is a file format for storing large genetic datasets. It supports both unphased genotypes and phased haplotype data with variable ploidy and number of alleles."""

    homepage = "https://github.com/limix/cbgen"
    pypi = "cbgen/cbgen-1.0.4.tar.gz"

    version("1.0.6", sha256="edcf856c9b0cafae7f6e999ed5d08aacdf1e09dadec766b79990fe5861e8cf7e")
    version("1.0.5", sha256="d6ca1f37762db9a3943fb17fb05f5539e296c836f40bfad21e61ad99801dd768")
    version("1.0.4", sha256="60719737ca40cc69577ed0c58b86a507638f311173ae21ae92fc185cc2b304a5")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-appdirs", type=("build", "run"))
    depends_on("py-cffi@1.15.1:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pooch", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-urllib3@1.26:", type=("build", "run"))
    depends_on("py-black", type=("build", "run"))
    depends_on("py-isort", type=("build", "run"))
    depends_on("py-pyright", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-poetry@1.0.8:", type=("build", "run"))
    depends_on("py-cmake", type="build")
    depends_on("limix-bgen@4.1.9:", type=("build", "link"))

    def setup_build_environment(self, env):
        env.set("BGEN_SKIP_BUILD_DEPS", 1)
