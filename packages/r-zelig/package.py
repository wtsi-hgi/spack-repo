# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RZelig(RPackage):
    """ Zelig is an easy-to-use, free, open source, general purpose statistics program for estimating, interpreting, and presenting results from any statistical method. Zelig turns the power of R, with thousands of open source packages — but with free ranging syntax, diverse examples, and documentation written for different audiences — into the same three commands and consistent documentation for every method. Zelig uses R code from many researchers, making it "everyone’s statistical software." """

    homepage = "https://zeligproject.org/"
    url = "https://github.com/IQSS/Zelig/archive/refs/tags/v5.1.5.tar.gz"

    version("5.1.5", sha256="fb06de2080bf4f598003ffa6a21d2fe4c5c0f6798d208d200bd65d697ebc0a40")
    version("5.1-4", sha256="0f10b5dc9edd2b0f5701339309b525ee26b3ee44a438e2e0639fd0f5b20bdbd2")
    version("5.1-3", sha256="a2e99ddc3d30f17329332ab0f25c4ad70ba7d870941d8396d8d4cc1da9e5ccc1")
    version("5.1-2", sha256="c3174df1cfe321c853b6494094af16920fd0e925589dcd6d62856a226dcb9816")
    version("5.1-0", sha256="2aacf24baace3fa2afbcf39f6181a63f52ee58401bb40e1f49016a985fa6c81e")
    version("5.0-17", sha256="470a56ed83436fdfe3db915165c6b7b22d248639f866af4835bfbb89c095e6c8")
    version("5.0-16", sha256="7e20d9800cb5d0af43d36d82d5cf42aadb7c01d3d7e42d978f390973877632c3")

    depends_on("r-survival", type=("build", "run"))
    depends_on("r-aer", type=("build", "run"))
    depends_on("r-amelia", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-formula", type=("build", "run"))
    depends_on("r-geepack", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-sandwich", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matchit", type=("build", "run"))
    depends_on("r-maxlik", type=("build", "run"))
    depends_on("r-mcmcpack", type=("build", "run"))
    depends_on("r-quantreg", type=("build", "run"))
    depends_on("r-survey", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
