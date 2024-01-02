# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGgpp(RPackage):
    """Extensions to 'ggplot2' respecting the grammar of graphics paradigm."""

    homepage = "https://docs.r4photobiology.info/ggpp/"
    cran = "ggpp"

    version("0.5.4", sha256="995fa9673b97340cec4ce321fe6161fe377f32bd20dad57bbef35c3900208717")
    version("0.5.3", sha256="8c351fbf1355556a20c5614bb8d3d9c73b7916ec973a70975b1271c1e9950cea")
    version("0.5.2", sha256="b3e25283ab68391bdbe82342d6bd012b00ea9e30099bdc746b30460f8f202371")
    version("0.5.1", sha256="6a8ef6dc8a54d3a735f01ee9f7c51f1d12c7ce289b40e7d02cb267be5f027b31")
    version("0.5.0", sha256="e750811c82ac878e084298ea198c48c5454e959df1b9e8ced969f3daf4b7bd7e")
    version("0.4.5", sha256="e98a9eb121de49c72fa58e5a093f72cadbab0b0be15b80d791ba7ff1dde6360a")
    version("0.4.4", sha256="616eba2c452fc5063ac0e5181cc71d61e28a9070eca420207abe6c25fb678a71")
    version("0.4.3", sha256="1fe2bcebe5615b4ebbbda0086cb17807d70d26e8c794a037449943cb7e99b59c")
    version("0.4.2", sha256="122ad3773ad2f33d85c2d81d9ce59d6761c32361a0b9d4fda71d778a67c25c54")
    version("0.4.1", sha256="d46f4dfaa23e5bbcfd5bcd502ce1e715293afec7ce77d34fbd6d02bb0d59489e")
    version("0.4.0", sha256="70f0726567b47d0508fbb3ff704534e61f0b2a6664188c727e1a8cdd9504f315")

    depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
    depends_on("r-rlang@1.0.6:", type=("build", "run"))
    depends_on("r-magrittr@2.0.1:", type=("build", "run"))
    depends_on("r-glue@1.6.0:", type=("build", "run"))
    depends_on("r-gridextra@2.3:", type=("build", "run"))
    depends_on("r-scales@1.2.0:", type=("build", "run"))
    depends_on("r-tibble@3.1.8:", type=("build", "run"))
    depends_on("r-dplyr@1.1.0:", type=("build", "run"))
    depends_on("r-xts@0.13.0:", type=("build", "run"))
    depends_on("r-zoo@1.8-11:", type=("build", "run"))
    depends_on("r-mass@7.3-58", type=("build", "run"))
    depends_on("r-polynom@1.4-0:", type=("build", "run"))
    depends_on("r-lubridate@1.9.0:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))
    depends_on("r-knitr@1.40:", type=("run"))
    depends_on("r-rmarkdown@2.20:", type=("run"))
    depends_on("r-ggrepel@0.9.2:", type=("run"))
    depends_on("r-gginnards@0.1.1:", type=("run"))
    depends_on("r-magick@2.7.3:", type=("run"))
    depends_on("r-testthat@3.1.5:", type=("run"))
    depends_on("r-vdiffr@1.0.5:", type=("run"))
