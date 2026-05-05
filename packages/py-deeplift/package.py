# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDeeplift(PythonPackage):
    """DeepLIFT (Deep Learning Important FeaTures)"""

    homepage = "https://github.com/kundajelab/deeplift"
    pypi = "deeplift/deeplift-0.6.9.3.tar.gz"

    version("0.6.10.0", sha256="ed0028a8de39bb052eedd80b3a29293a7190daec562a5a47650221e33cbe4f43")
    version("0.6.12.0", sha256="e39767cf9aad7cb422a1ba59875a2054ad3a521b59c2d44bb9f715a62ce80608")
    version("0.6.13.0", sha256="354ac5a00630b2df0856e8c948262e38c7eb83a719f71d6b5bf8ec4b064cb432")
    version("0.6.6", sha256="a868041ac5ad09b2a34a71975a99a6644973a35d6663fa1a1da4d67373743faa")
    version("0.6.6.1", sha256="d16f9e33740fe43cea63744c475f8fbc33eedbf1ad177e42605b749b727e3d7e")
    version("0.6.6.2", sha256="69113712062eb127b0e1dd055e49e2c5aa990d9e75c6cafd6a409e4544fb5041")
    version("0.6.7.0", sha256="770f8503b797a04a6737441de0ef05f1714dbe426b5e9839f27ad33b3c88f42e")
    version("0.6.7.1", sha256="4faa0e44c772f8bd132b30e4fbd517ff3d5ef3aef8c68d7f621c88d6d7de82f8")
    version("0.6.8.1", sha256="119ff1ad26ead029fe68611458bf33b88f4b260412e6c609877d1bc416e05b67")
    version("0.6.9.0", sha256="f38e07475067f0b811f8e18fca095d0caa82b2561f690019a65bf766c9352d53")
    version("0.6.9.1", sha256="3660995ff7c1d260c3173d6fb4ac04167ee3490578f48092ef44a78516dcbd72")
    version("0.6.9.3", sha256="4ce59e995e24d958832f8e406358d41449bf91eeb5dad39f903d6ff8c54854bb")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-numpy", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        python("-c", "import deeplift")
