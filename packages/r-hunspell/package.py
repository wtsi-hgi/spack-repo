# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RHunspell(RPackage):
    """Low level spell checker and morphological analyzer based on the famous 'hunspell' library."""

    homepage = "https://docs.ropensci.org/hunspell/"
    cran = "hunspell"

    version("3.0.3", sha256="fdaa1473a62dff2a5923b9bd958d87e546069ca22ce113f44e88c761338442f3")
    version("3.0.2", sha256="5ea25955f76cc275e56424c8ac0700d1cb1f5c21c7f8d61c25fa740d731a324e")
    version("3.0.1", sha256="1fedbb913bc13c790d2fabfe4edda0a987db3a078bea8c0ca9b777d20af08662")
    version("3.0", sha256="01fb9c87f7cf094aaad3b7098378134f2e503286224351e91d08c00b6ee19857")
    version("2.9", sha256="33e6fa939f3458d151cce1855c6743e850dd736f111ca29668de1a4d48312880")
    version("2.8", sha256="2bce7eb316900294acb7380783818ccd922932bcac3dafed6940a04c3e598c27")
    version("2.7", sha256="2e5e2a56dd88122747c07609805c1d0c2d45ba05cb7ed656e6d080fb6e07aa9a")
    version("2.6", sha256="78ba41924f8021241f43efbd2befbd72a79ebbbd9bc3a4a0794fb09af468e70b")
    version("2.5", sha256="17e83c287ff2da6e703a2ea139206daf3e93714c83d76616e8a710485f94ba5f")
    version("2.4", sha256="ffbed7a0928685ef067d76746007937d1c062fbe7b7c50d75229588500cb6ee9")
    version("2.3", sha256="52de433bf928cebff282518626379416798682e2d88f46855b2260f792d2f2e9")
    version("2.2", sha256="311579b872620759f2cfc358b49bde462139db979bb38a58b98cf8c36523ffbc")
    version("2.1", sha256="5cfa6d471d92334b7fb20f3524fe5cc14a3e5782260994b0079656cb94747bfb")
    version("2.0", sha256="ef7722f7b80f00d8addd636587ad4b1b1db48ba79eb3fad46d8d47e570c13041")
    version("1.4.3", sha256="6f42e1ed02cfbc83a2efd0bc291ef35d7de5ff542637c511c515cefac53d6ef1")
    version("1.4.2", sha256="41e8695ff5d0f5259af8d7f16c0d5c1327d04e0a182d230eefc972524e2d722c")
    version("1.4", sha256="8df975b63027bc7cdf360977b3be1798c1b3979edb261f460a396f23bacce029")
    version("1.2", sha256="bde844d8c7f92954421e1191c9ba61a06a6815063572be011474cec4625a2b7a")
    version("1.1", sha256="269cfbf90b614fa71a4182b9e8ea888605d9653baf23d0f71dab53c09eb485f6")
    version("1.0", sha256="860d116ecd42017f4ecf9b9dec4becd1f08f9fc20ac641d5e59d79f72e4a84a6")

    depends_on("r-rcpp@0.12.12:", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-testthat", type=("run"))
    depends_on("r-janeaustenr", type=("run"))
    depends_on("r-wordcloud2", type=("run"))
    depends_on("r-knitr", type=("run"))
    depends_on("r-stopwords", type=("run"))
    depends_on("r-rmarkdown", type=("run"))
