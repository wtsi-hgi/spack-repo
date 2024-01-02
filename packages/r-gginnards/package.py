# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGginnards(RPackage):
    """Extensions to 'ggplot2' providing low-level debug tools: statistics and geometries echoing their data argument. Layer manipulation: deletion, insertion, extraction and reordering of layers. Deletion of unused variables from the data object embedded in "ggplot" objects."""

    homepage = "https://www.r4photobiology.info/"
    cran = "gginnards"

    version("0.1.2", sha256="5c2d61936fefee5fef00a9a8eb33a470404fa0a134079944ee9bfbb8085c9cfc")
    version("0.1.1", sha256="16aa799376c051b4f6acbd68db29f9bb22a3a5efa6a36691268a8d63954f8f67")
    version("0.1.0-1", sha256="5d0a37295b3b2b067daeca4d9334753e9692fa52872ddca09a58f959b5cefecd")
    version("0.1.0", sha256="29764e1cb6f2f6bc1e2be42915af31cd57c94ce3c1b0b81cb95956ff484f6151")
    version("0.0.4", sha256="ff047ff015f67d3b85b965cd8a21fa1735cd0ac45de39f255beb400aba4ad2b8")
    version("0.0.3", sha256="be1f409049e7a70fce7a6a071d645dec33276a36670c44eec64e342d39429e96")
    version("0.0.2", sha256="5331f4613d4341f6ae168bddf734c642a5d65d82687ab9820e2c592d6eae4481")
    version("0.0.1", sha256="187adc6588af612f203b564da2e2038bf59c7f9f372c1a915a8a1118bfc3c5fa")

    depends_on("r-ggplot2@3.3.1:", type=("build", "run"))
    depends_on("r-rlang@0.4.0:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-tibble@2.1.0:", type=("build", "run"))
    depends_on("r-knitr@1.24:", type=("run"))
    depends_on("r-rmarkdown@1.14:", type=("run"))
    depends_on("r-sf@0.9:", type=("run"))
    depends_on("r-pryr@0.1.4:", type=("run"))
