# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSee(RPackage):
    """Provides plotting utilities supporting packages in the 'easystats' ecosystem (<https://github.com/easystats/easystats>) and some extra themes, geoms, and scales for 'ggplot2'."""

    homepage = "https://easystats.github.io/see/"
    cran = "see"

    version("0.8.0", sha256="62b68be6616be15a54feef2388d65fad1049327a67e6f59579cbe606c086bded")
    version("0.7.5", sha256="9f8b497bf26ed6f528d1291727fdc412481f9d7ddf922620b4bbe2034e25f1bf")
    version("0.7.4", sha256="82784499a088f29cd1d1ec99481d121ddea1c0cbf334ce51e7f9ff103054e21c")
    version("0.7.3", sha256="5f3817ea30d25a36dd2e28c80e1d9ccfa7468f8899c1e2131a7b3d5bf145f94c")
    version("0.7.2", sha256="3ebb8d817679d73a946947c9a3572b235700c0b4ac06f4a4af0ff0377968f0c8")
    version("0.7.1", sha256="2d7f006ff5e07932530cdda0ee64875f50ce3ee578d68890333dfdb1cd7b13b5")
    version("0.7.0", sha256="c7d1e5724a6e9c600c47808346ffea1d6fb1a3efef61e23bbfeeae4e6f2d71b8")
    version("0.6.9", sha256="04e3cdbd756c6b8f475dc78b6489b54f4ff5d993d4a8a78d755f4bfe476d8264")
    version("0.6.8", sha256="72928fda76133a8a3ee7ae1ce46454d316d021011211a779c2fe564dd272f060")
    version("0.6.7", sha256="482ede4689eea2fd8ba9f59aed902aae95dda7e9e5e654ba2fe70e699c0cc271")
    version("0.6.4", sha256="ca97355ea0ec6f831da1b76ee2950320c866b721e8d042dc62934605d0f49775")
    version("0.6.3", sha256="53bae1e9a4e023dd1a96905e495414c764badd2cffedb17087860acfa53b6c76")
    version("0.6.2", sha256="6f80ebd08b3fc6a270450fd3e8f772760e970011a84d903ae62bf75485eb4c54")
    version("0.6.1", sha256="80e8a4fb61d02e978ce60362413d78da87738987f5c53d54327674b58df9ed2a")
    version("0.6.0", sha256="5ff297f0b81207d75e15cd48e57c6c536394b01d37f850404de4a7ac67eb14ac")
    version("0.5.2", sha256="64462510932bd94c9bb6920336a7daf0318f5e453a28c014e01babd26e8cabf3")
    version("0.5.1", sha256="2a30fbb0c9c765b217fff2a7891e565620a4b23dd8754ea023b86be6039a86ea")
    version("0.5.0", sha256="3feeb48255312ef1316e61c99bcd2b1b98911579bdc52e302b1cea1223de7e73")
    version("0.4.1", sha256="b1ea12ff33a5d3704be066afa238bf1c2edd39ad3788468fa8789d9534966270")
    version("0.4.0", sha256="c15c8f99264a56c85e8bde837cf48af5c2cc8f4c481d3d91e3ae65490769d5e2")
    version("0.3.0", sha256="411bf3bbedd677401d4efc270290a6294be3389569207389574ddcb3c5769661")
    version("0.2.1", sha256="32c60e125da58540aca927fed3ef749f6d36d601dc4e026e46377e30fae09030")
    version("0.2.0", sha256="497a399b853542a26d02606545288e5f3eebf1728e785e99aa7814b9ffc08d2f")
    version("0.1.0", sha256="49edeb3e348f5f8e5f3849f216d3a9b246f5d983cdbe691818d674432a66ae0e")

    depends_on("r-bayestestr", type=("build", "run"))
    depends_on("r-correlation", type=("build", "run"))
    depends_on("r-datawizard", type=("build", "run"))
    depends_on("r-effectsize", type=("build", "run"))
    depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
    depends_on("r-insight", type=("build", "run"))
    depends_on("r-modelbased", type=("build", "run"))
    depends_on("r-parameters", type=("build", "run"))
    depends_on("r-performance", type=("build", "run"))
    'bayestestR', 'correlation', 'datawizard', 'effectsize', 'ggplot2', 'insight', 'modelbased', 'parameters', 'performance'
