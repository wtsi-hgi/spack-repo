# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelbased(RPackage):
    """Implements a general interface for model-based estimations for a wide variety of models (see list of supported models using the function 'insight::supported_models()'), used in the computation of marginal means, contrast analysis and predictions."""

    homepage = "https://easystats.github.io/modelbased/"
    cran = "modelbased"

    version("0.8.6", sha256="e8b0337c0044bad72c589da8e223c7235833f965b76005860583651b55851251")
    version("0.8.5", sha256="744c65304fdc4105d133003791af82c194f0e4920e1b47c19d9b4cb6486aa5ba")
    version("0.8.1", sha256="c68b4fdd2ad1465c20780ae26877ab4dfd15c448858bca44169fa53d891ce0d3")
    version("0.8.0", sha256="2a2c9cd7afd48c9d1c113b2564a6e7f14259c389e34a9cba52b30c001fc0873f")
    version("0.7.2", sha256="8ef0c0ce5acb1a7ec8d8524a436eae85ab35620f3ce8b1c5e0462c554cb97caa")
    version("0.7.1", sha256="81ae095ad9ba19aba1e7017a4a6a6895a3738e9f6e9adb1383866ff007a7c7bd")
    version("0.7.0", sha256="df0d3dbb9e044aa6b85caf78d9f49d04f266ab6f378ba16de4f8e8adc4fa094b")
    version("0.6.0", sha256="b2e263c5d9a017705dfa73ad66a3807a2c55bcd86ca23acd73e2165c64c1860a")
    version("0.5.1", sha256="22b160b02fd18de1524fc1996fc13b86916def85a66be2049dea3a5c1aa01d55")
    version("0.5.0", sha256="1bcdde1bbd9b128215c6d9bd201eadafadcdc6894fc07693242dff711190115c")
    version("0.4.0", sha256="902b7d5b963e6c86bd3e5e9ea15169af7f583070d57f47f3fe3f9314bb7810c6")
    version("0.3.0", sha256="1eddcbdfb1be5c326b813aae0c6effca1f86b6311dbd4cf5a2c5589054fc9f50")
    version("0.1.2", sha256="1ca60e8880b783ec81bea98acc623a649a05965733ea0ef75e6e277e27bb8010")
    version("0.1.1", sha256="3e5ecd7ac235f5012d068ab11718e54f2d92d2f794f548b7cd536f67cb119321")
    version("0.1.0", sha256="7de99dbeb24005d0eb0314d6412947363242bf4609d17de0d8c25e334a4d224b")

    depends_on("r-bayestestr", type=("build", "run"))
    depends_on("r-datawizard", type=("build", "run"))
    depends_on("r-effectsize", type=("build", "run"))
    depends_on("r-insight", type=("build", "run"))
    depends_on("r-parameters", type=("build", "run"))
    depends_on("r-performance", type=("build", "run"))
