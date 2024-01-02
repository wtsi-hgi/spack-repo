# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RDplyr(RPackage):
    """A fast, consistent tool for working with data frame like objects, both in memory and out of memory."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://dplyr.tidyverse.org/"
    cran = "dplyr"

    version("1.1.3", sha256="6843a247db0fcbba6cbffc869efbdfb25247ee6cf2fbdc36fae7e36cccfe1742")
    version("1.1.2", sha256="c220c38a3a44977c43eeae3d9aef90e8bb297150cad0993ea8d3cc13150096e3")
    version("1.1.1", sha256="dfdc24bdba38c091edcf2cc3fa58267f4ebbf7ea1b3b715b1ada7a1be6d5bbf7")
    version("1.1.0", sha256="8cb0535e49dd40b3054046735738f1e48507ac9a56b015d16ebcb54593b84ed7")
    version("1.0.10", sha256="3ab639f627b4e439052df18f193f0ccab223225a4ae2ff8c18aba4f9807e0f2b")
    version("1.0.9", sha256="e2e1f7312618b4e32ada9a1da79cef32eaec12acd408c973a6b069c6be4fb46b")
    version("1.0.8", sha256="3b6aa3a06d67037223da6af4b59ab89cbd342bc450b92c6050fb267127236075")
    version("1.0.7", sha256="d2fe3aedbce02fdddce09a8a80f85f5918a9d1f15f792ad4a98f254959d7123d")
    version("1.0.6", sha256="088c381a19595b202d5508003168c302fb6d893c9e7164e17ddb71616162fa07")
    version("1.0.5", sha256="7541a09c66ecb40736e25bc9ec9591f26ec4ee67c99823b4ac855760b5c96e70")
    version("1.0.4", sha256="9bf68f71d1519432bad08089fc254b872c990c5a40b32a7e63b03d49f88e093a")
    version("1.0.3", sha256="28a1a9d87e99154d4d1542ef9da9fd70f869a173dc9709f4583a5770bae58441")
    version("1.0.2", sha256="7cb1329fbf5c9609ca300f695fdfae67198b6b7273cf81b71cfc01c12d0adc4a")
    version("1.0.1", sha256="55f757adc122dc39009739c03a32c8182e6e2f7ad697fcc0711ee1e56cf80d3e")
    version("1.0.0", sha256="bfb65131cd24d891e671999be29e6dfebb3eefa41c262dbc7a13d7c0ff3db1f3")
    version("0.8.5", sha256="5750d3bf4bda7b5448e08af264ed183b4f7bd0c59a9d828fe9dd399b14590218")
    version("0.8.4", sha256="811803d5f13eb21ad8811060da384d92fe7489714014c5959deb2f8977ada0d9")
    version("0.8.3", sha256="68b4aac65a69ea6390e90991d9c7ce7a011a07e5db439d60cce911a078424c0c")
    version("0.8.2", sha256="e2b6d5b30d04d86f270374623da426541cee8e33ce446fcab6cd7862abf8e18b")
    version("0.8.1", sha256="5f3ef7f0378d89799d466be254e25857a2747d70d5d97450618ac9303f1481db")
    version("0.8.0.1", sha256="8408889d31a32527dbd846b3a6d995a2a7db7a51618ff28e61747afcb25ccd5c")
    version("0.8.0", sha256="43b884c5dcdefd9e03c9ab3a54206de982633e850564d73e08b1dd68f8952186")
    version("0.7.8", sha256="37799ac5734d14b14ab9594ddec7f79e9a798907b87ff8b2d281a148a14de51a")
    version("0.7.7", sha256="0553db5a55f0e6f5d2d111e88422c6d26e9d54cb36b860ad2ca28e3826e3d4a4")
    version("0.7.6", sha256="d489cc8b53854ec30737bb7d39b331b67ca35f4275ad19e97420d7a247808330")
    version("0.7.5", sha256="2fbd8f316a59670076d43a0fe854654621941ee5f621ea5f0185a3f5daafda50")
    version("0.7.4", sha256="7b1fc90750fbb46483423da6721832c545d37b157f4f3355784a65e50fada8c2")
    version("0.7.3", sha256="ae67ed4f629a74485626b8291b5219b81ee6fc4c5fe5a077bfbdfeae59dee573")
    version("0.7.2", sha256="2262d1ad9fefd5c7d1030dea0edd6ffe5747b827cabe088cc915b0a09818eb4a")
    version("0.7.1", sha256="8c7573464b2a808f711f8977d0039e043318f93e47f2e80ba85b1f4ca09d12f4")
    version("0.7.0", sha256="27b3593c09da5e99c0c4fb19ea826edd2cab619f8aaefd0cfd2a4140a0bd9410")
    version("0.5.0", sha256="93d3b829f1c2d38e14a4f2fa7d6398fc6c1a9e4189b3e78bc38a0eb0e864454f")
    version("0.4.3", sha256="8c364c7baed0710004f3b68cb6ed430ac7e4a08afcaa0608123d7b72895d19dd")
    version("0.4.2", sha256="a665277738944f117b7bd7a8e75233c0e9afa1475b8f51b32ca1acffd45916ac")
    version("0.4.1", sha256="bc324a9b64e851800489cdc29e9ee3e90babc5b2937fe576f87cff27447a9c4d")
    version("0.4.0", sha256="d2d7782010bbbfb9ac1b339f17e88ca2c1426f09ce4c6d19b412392608f8e7d3")
    version("0.3.0.2", sha256="3c5f970c91bf44eb3f1a99c192468216a20bd1e1e4e323aa98266e0c50be8bac")
    version("0.3.0.1", sha256="fa6aec1f3545f757674b802821f16aa4b0017a4b278b061af6be4852a4304335")
    version("0.3", sha256="b93bf45b4217d5bd0a61ff15928f44f4f147bc7260ff45ac3b4bc283ee323434")
    version("0.2", sha256="38f45b945f77d985edbcddf1fb53ca35f9bbd58f302b7c6b73cf6e2c2cf16b12")
    version("0.1.3", sha256="838fa5b37fcfbc62805780a7704b09423764525924b23de5d1b30e60417cb681")
    version("0.1.2", sha256="7f07fd4b655c023337352a2ab97e58290f893f3780ec00650a107bf0e5619653")
    version("0.1.1", sha256="fb41f39fe3365478e48b3d09bbbfcdb5d9d0982877ad4be97b47852f43b538a7")
    version("0.1", sha256="dd669fe70e2c49f046811d0328143278fe4f596cbe18e945bce33262e8b76488")

    depends_on("r-cli@3.4.0:", type=("build", "run"))
    depends_on("r-generics", type=("build", "run"))
    depends_on("r-glue@1.3.2:", type=("build", "run"))
    depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-pillar@1.9.0:", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-rlang@1.1.0:", type=("build", "run"))
    depends_on("r-tibble@3.2.0:", type=("build", "run"))
    depends_on("r-tidyselect@1.2.0:", type=("build", "run"))
    depends_on("r-vctrs@0.6.0:", type=("build", "run"))
