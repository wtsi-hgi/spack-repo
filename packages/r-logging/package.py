# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogging(RPackage):
    """Pure R implementation of the ubiquitous log4j package."""

    homepage = "https://github.com/WLOGSolutions/r-logging"
    cran = "logging"

    version("0.10-108", sha256="85c91aa5a313f5f9fbb0394cda3f924a2495cca3cc5cd68dde0695fe3c20ed8d")
    version("0.9-107", sha256="b7194178d1e29bee6f8673bc5b6073bfd334707457563f3c96df580cb2226f62")
    version("0.9-106", sha256="7a35a537252353e6c18066f2c05f045a0f814ddbc853720303a98cf1943bd5c8")
    version("0.9-105", sha256="cf265b8125338c6f6f5ec74f4c7f800e9e93bf326522157053d7b093000cb58c")
    version("0.8-104", sha256="3d46b00a436700635878edec954c7d962bea93193f61af673895220b3d213dbf")
    version("0.7-103", sha256="aca8153206cc815a49470844c48f44f84e6d7a6ce52686a8593f727582c0e7ea")
    version("0.6-92", sha256="7bf41060e4930800b5a4799c9a6cef21a4d18f9df85958b51c807a30277c9b58")
    version("0.6-85", sha256="deb9cf4456040e8b7ab602a5fade8e924bad0f7a10f50e3e9a09cf82a2d73679")
    version("0.5-63", sha256="4d6572ba1cdc161a198da5f5bd41470f71080a533f205c6d1be446bededdf3fc")
    version("0.4-42", sha256="71c696386d8a301486d8cdec4fdaa376eb04c3c46ab1367234f7ba0a91a5d69b")
    version("0.4-35", sha256="de331fb59c9daf1ec03a6afe74382d3a805676b4ee0334dc004bbad261bf35db")
    version("0.4-13", sha256="19a0d7d780e7e97a9236504ee8212786cdddd438020f41c46500623d4d2c034c")
    version("0.3-9809", sha256="f0d7b7cda8d00f6bc8c0fdf39eab615eab3f6132914b0a5f9a24e99a47f6cdf6")
    version("0.2-9100", sha256="99d918ab54d7a523a44737357ab457969f1d38d540a3861612341bf591081c66")
    version("0.2-9014", sha256="d50b604564078e79c1e4717415982a93fd3e75ed2874d8f77e2cfd02b030c3be")
    version("0.1-8996", sha256="5935899418e8a5b524a77497e4fff93b8dc2c8cbdcde9a757942ba11c2b20030")

    # depends_on("r-foo", type=("build", "run"))
