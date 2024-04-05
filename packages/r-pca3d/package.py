# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RPca3d(RPackage):
    """Functions simplifying presentation of PCA models in a 3D interactive representation using 'rgl'."""

    homepage = "https://web.archive.org/web/20220615221126/https://logfc.wordpress.com/"
    cran = "pca3d"

    version("0.8", sha256="c6c21761adc70e47040dc8138dbe9db5a44341daa0f689fce22ea87a1db3f00d")
    version("0.3", sha256="a0510b3f85d01aabe8620dc2b216af096f23ad8533238c82a7769d8ccc25cc06")
    version("0.2", sha256="99b2c1037576e2bde92298c0dc22b713962d0ebafa2d9121195bc647588aeef4")
    version("0.10.2", sha256="a6cbc3d57cdf89ac9cb6b7ce48ab8cd9a929b092425ee35c3fd8c0f6d1b1f476")
    version("0.10.1", sha256="a4cda65f269537708b62bf517faace643386d7f72ed2be03a4ff6d084bbae7bb")
    version("0.10", sha256="c3e95f50a4d1bdc6b48ad18bc496131bd1601ec2502e5f20684ec0239726f5ae")
    version("0.1", sha256="dcd05beb65ce8ecb5e78dc4c70d6f149b7200d1da82690dc014a597f658a9e20")

    depends_on("r-rgl", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
