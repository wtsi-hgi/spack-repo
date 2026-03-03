# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStone(PythonPackage):
    """The Official Api Spec Language for Dropbox."""

    homepage = "https://github.com/dropbox/stone"
    url = "https://github.com/dropbox/stone/archive/refs/tags/v3.3.1.tar.gz"

    version("3.3.1", sha256="dc5aff3fad1333188d4ddb4eee0a19d31e6262bb3cdf10c0bbdaeb309ff91a52")
    version("3.3.0", sha256="48b1a29b271fed237a6a1087bad3cca938f58c1650c69c35322ab14a2969c01b")
    version("3.2.1", sha256="05a6c9fec0b923a5e54814f31365499d6e7b726aaddfe5b8ee2d1a4b6cb06d3a")
    version("3.2.0", sha256="23bf8edb26a6862990e1f88aa1907521d4346285e1997e1bc390616669ca57df")
    version("3.1.0", sha256="362d1151b10597fcafd6b3b9ecf10b55b0aba5bd2e74465a04e59e4e8c040540")
    version("3.0.0", sha256="52c30b46e75fb3bbe50db93d528ebbd40985049d091fefed2208450457a52043")
    version("2.2.2", sha256="9e903b04091cfe14168c506556a80d58babd9a17e03dd8258a0ea517ad74154d")
    version("2.2.1", sha256="28715cea55cdb0905cf34e48b1ba056591cc015a5749205f7dc8ab9b36290424")
    version("2.2.0", sha256="43a8d7b4c7e2a0d89a84a7e8eed34fc105252dec282521d2e4a5e1ca843110c6")
    version("2.1.0", sha256="1088c9d7e33c79ef624ce75f9441c125f4eaded074101b02c8ea56714a8dca39")

    depends_on("py-setuptools", type="build")

    depends_on("py-ply@3.4:", type=("build", "run"))
    depends_on("py-six@1.12.0:", type=("build", "run"))
