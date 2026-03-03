# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install drop-seq
#
# You can edit this file again by typing:
#
#     spack edit drop-seq
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------


from spack.package import *


class DropSeq(Package):
    """Java and R tools for analyzing Drop-seq data.

    Drop-seq is a technology to perform single-cell RNA-seq experiments
    thousands of cells at a time. This package provides command-line tools
    for processing and analyzing Drop-seq data.
    """

    homepage = "https://github.com/broadinstitute/Drop-seq"
    url = "https://github.com/broadinstitute/Drop-seq/archive/refs/tags/v3.0.2.tar.gz"

    maintainers("github_user1")

    license("MIT")

    version("3.0.2", sha256="8a128f0ca7799d6500c9ae8978157474f4189e0a8885c4eabb3f29b68d483921")
    version("3.0.1", sha256="cc053a57419ab90440a2fc292f141e17fabb76a0471b88d9ea426f53e4369d53")
    version("3.0.0", sha256="e9150edb5bc076a371d15cd9d681d5557314ab8f6c74bff8f88c1fb49eb80682")
    version("2.5.4", sha256="aae239fdff4caaa33b6f9b34315b4037a14bf22cdc04be7ceaf7870edf6e8eb5")
    version("2.5.3", sha256="6348c14b46e830c51be5fa5373e14e0ee566ef4e390dbdfb0d32be79e84af024")
    version("2.5.2", sha256="704f63487fa53fc30ed1f5a0fdbaee1208d5047716c89bab604439564a371109")
    version("2.5.1", sha256="72beda623b4ff41db5d2b1c4591b8b26707387acb95d1cd18afaf54341b2e4fb")
    version("2.5.0", sha256="3b48475ba08bee931be20bfd31ef4ca5ac2e61e5cd253bb41d90f7b6daf8f572")
    version("2.4.1", sha256="80e1415ff6db9efc715249afafb7864cea54712570bc11f723fb9855e67467ce")
    version("2.4.0", sha256="2857e2c1024a8709269cb047434e565b6d121124eb907e303eb38eab01e7a843")

    depends_on("java@21:", type=("build", "run"))
    depends_on("r", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("LC_ALL", "en_US.UTF-8")

    def install(self, spec, prefix):
        gradlew = Executable("./gradlew")
        gradlew("distZip")

        # Extract the zip file
        zipfile = join_path("dropseq", "build", "distributions", "dropseq.zip")
        unzip = which("unzip")
        unzip("-d", prefix, zipfile)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.dropseq.bin)
        env.prepend_path("PATH", self.prefix.dropseq)
