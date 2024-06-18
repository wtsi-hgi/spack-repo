# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Mixcr(Package):
    """MiXCR is a universal software for fast and accurate analysis of raw T- or B- cell receptor repertoire sequencing data. It works with any kind of sequencing data:"""

    homepage = "https://github.com/milaboratory/mixcr"
    url = "https://github.com/milaboratory/mixcr/releases/download/v4.5.0/mixcr-4.5.0.zip"

    version("4.6.0", sha256="05db1276951a2e656d0a7bf4e2b1fff326733a5f961a9d4829be139852fabe13")
    version("4.5.0", sha256="4a92a61b9a87a569636c898b8c3fb56f173884d06dad5906be5a0cc6c71dfe2d")
    version("4.4.2", sha256="0dcda83b6aacb715bfd9cebb95aee4e018fb125147a8ec806acf3167f07cdcba")
    version("4.4.1", sha256="6b58b83ecf6cb7a7b100792f93d4d318429e32e5404303814446c9ed4dbe16ed")
    version("4.4.0", sha256="4ad656cfb293d58a1463cb8546f1832a065527bbc46dc137e64778539a7fcfa4")
    version("4.3.2", sha256="8f67cda8e55eeee66b46db0f33308418b6ddb63ca8914623035809ccb5aae2c2")
    version("4.3.1", sha256="98f9a1480df0db07189932db0095b933f4f9e5d03aa4b669fb687a4fef2609c6")
    version("4.3.0", sha256="76c17d9f66b423c6d2335b1597cbd5893b08952354be431a4c9a1034c5c3ca0c")
    version("4.2.0", sha256="b72515e7cf6f82424acb702b07df22f7dea5bef320f09360b9b6868fe7f43eec")
    version("4.1.2", sha256="df94568f777aa2a0f05209904c179cbedd87afb3f88c12024538c92a5a44a859")
    version("4.1.1", sha256="0486b33a9d9379956da95f30cfc46e2a237e1231155a323210700c29bf7eb4e9")

    depends_on("openjdk", type="run")

    def install(self, spec, prefix):
        mkdir(prefix.bin)

        install("mixcr", prefix.bin)
        install("mixcr.jar", prefix.bin)
