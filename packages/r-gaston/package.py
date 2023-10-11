# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGaston(RPackage):
    """Manipulation of genetic data (SNPs). Computation of GRM and dominance matrix, LD, heritability with efficient algorithms for linear mixed model (AIREML)."""

    cran = "gaston"

    version("1.5.9", sha256="07fb9be3142626550d12b4a9eb821c04c273bbe44f40bdab0e3c934b74c997b8")
    version("1.5.8", sha256="8c09f2cc721a03f7ffdf2cef351e0ffd9561c5c1eb75074fa373bf81353b63df")
    version("1.5.7", sha256="3188dc7fb34c30d43f8601432c805bfb6603cf8c891f2e767ebb114b6f23e993")
    version("1.5.6", sha256="2f9b8f8d16c20cfa3426b57aabf1d63a9e9ab6e4689f0fec1e8ea6251d8ea6af")
    version("1.5.5", sha256="ffcb098bc0d39f8549431897be49ffbccaacd29885b7c8dca700119ab9193e76")
    version("1.5.4", sha256="19c4226ff405ddec9fe1475fb8fff3547bcaee8b3ee3179abb5331f3010854fa")
    version("1.5.3", sha256="954790ee9c753d12757211c9d470b7b20926aba29d2b6142a833ae6ff5cb8978")
    version("1.5.2", sha256="70609cb2b1833f6e35a8b92b1683e90c2b6f225dfc0da0f2d34c6b739f540c9c")
    version("1.5", sha256="bac68f418da438536be8673d98e248129a79872a05a2a37c4b6797f19c0497ee")
    version("1.4.9", sha256="7fafacf437ba46c584068d51ee77a60eb7104095913b5770483b8381e931cb8d")
    version("1.4.8", sha256="b713d45be73c4b758e016434e45460c7b751535c68d271761d9a19c486463284")
    version("1.4.7", sha256="583666ae28c1fbb554866dae8c3e0092e26ae10cf631762bc7196b754a9d808f")
    version("1.4.6", sha256="cf6de78363d22f92bfbf3ed13d0cdc55160f3fd84a2ca1e67998e84ebed3558d")
    version("1.4.5", sha256="08bd1f59a36ce6d14e790cb00321f8166f6fe72d7db84b1f68a531f28c9612dc")
    version("1.4", sha256="f51389c4c2aa0a773486b4f9dc34a9b809e47306f18ca065458ae8d72a5a02af")
    version("1.3.1", sha256="29707c52280d3638dc7c4f17be6ec439331f7c6838bcc7cbe6cf7d79937a874a")
    version("1.2", sha256="72987443df45767da959058c4808572f8fc2ca152162e5287e16c92bf9408eeb")
    version("1.1", sha256="1e87f35e5b36c05662a0347521d01ad0cb7d772373f6e06a032ffcd6cf93d6b6")
    version("1.0", sha256="701e8bd0879af9e061d344e50944b891ceab06d8877488e2ba00f605fac6f4b6")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
