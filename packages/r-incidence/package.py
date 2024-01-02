# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RIncidence(RPackage):
    """Provides functions and classes to compute, handle and visualise incidence from dated events for a defined time interval."""

    homepage = "https://www.repidemicsconsortium.org/incidence/"
    cran = "incidence"

    version("1.7.3", sha256="e70bd75ce86841ed92fbc316784a392d17f2f53e11c4895d0aa4327dae80bdf1")
    version("1.7.2", sha256="d545472025626175388505f7642de8b07828fed3d28d492d2751f2b29c38060b")
    version("1.7.1", sha256="c45bdae56cd0a2b9d8d579b13708eafcbb106f640d054695041e3d526f68e6b4")
    version("1.7.0", sha256="4397697a2eff1a97bc265dc70cadc3ec914acdf134ec2ec2c58738dde14d56d2")
    version("1.5.4", sha256="f9c173f5cf5a5bee0c3e64a67a2103acb1b63ce1fd61b0f8322732c77fd565a8")
    version("1.5.2", sha256="5b38654872173adfa380ee6bf0afec4458f1164e43979966750caa9b3c26b7ee")
    version("1.5.0", sha256="67e215cf18ed19fe5df50df71019a5e5eec0f8c6262d192ee37c2ebeea20cc9c")
    version("1.4.1", sha256="28fb4535454ed8f37edbb7a120f5df57f0ac462a6b75c237a1ad5e48210a858d")
    version("1.3.1", sha256="bcab4f8f0a2cfbdeabdc1b1a006970cbfe5c5256ee4a0f7d4b31b1476a74d463")
    version("1.3.0", sha256="6181484016823963d2dca0cc17deeefde93a6993f4fd10ff2b64a6fa9ea50ad8")
    version("1.2.1", sha256="3e9e83ed950bd5cc04c952f7551f5226aad0a70f10e23f4f6055f6ec35634b3a")
    version("1.2.0", sha256="23a34635edeeef3f843fa10cf6ede67e444c18f946034fb1d442fa24150ee3f8")
    version("1.1.2", sha256="83e392b2ad49141c2d4cccbab1f85f55488eae3946de69f5298fe3667fb1d4f7")
    version("1.1.1", sha256="048ac6b179ac56597d1201b5295b22f8fd161b6c9d2ab569615ed96a3e7eb40d")
    version("1.1.0", sha256="37a5b879381e271ca0dce0d0c49b66611447472b5525993bd0d816ab6565b1a3")
    version("1.0.1", sha256="a4ba3eff4d7989bccf60d025e09b54e41a0e90699bab004f53e79d6252519d38")
    version("1.0.0", sha256="b48a4ddfd358da7281346bdab35b4748389550dee128439221cbedb022d1530d")

    depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
    depends_on("r-aweek@0.2.0:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-outbreaks", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-vdiffr", type=("build", "run"))
    depends_on("r-covr", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
