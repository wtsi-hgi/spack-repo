# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RBactdating(RPackage):
    """Bayesian inference of ancestral dates on bacterial phylogenetic trees"""

    homepage = "https://xavierdidelot.github.io/BactDating/"
    url = "https://github.com/xavierdidelot/BactDating/archive/refs/tags/v1.1.tar.gz"

    license("MIT")

    version("1.1", sha256="838a26221b9c6cd71b51cd3535285fbce3b9ee04612c80fa5df75812506d49f2")
    version("1.0", sha256="add9c391709e4d340d173cfb29d30ec6815d5ce89ff8038cea981260be01b151")

    depends_on("r@3:")
    depends_on("r-rcpp@0.12.13:")
    depends_on("r-ape")


