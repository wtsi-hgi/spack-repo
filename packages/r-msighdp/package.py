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
#     spack install r-msighdp
#
# You can edit this file again by typing:
#
#     spack edit r-msighdp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RMsighdp(RPackage):
    """The goal of mSigHdp is mutational signature discovery using hierarchical Dirichlet process (HDP) mixture models. mSigHdp is only supported on Linux systems. Most users will use the function RunHdpxParallel."""

    homepage = "https://github.com/steverozen/mSigHdp"
    url = "https://github.com/steverozen/mSigHdp/archive/refs/tags/v2.1.2-bis.tar.gz"

    license("GPL-3.0")

    version(
        "2.1.2-bis",
        sha256="5f6c95f9aaf795132190139b584b73f07877df4082d157a35277be5ca6f3ceb0",
    )
    version(
        "2.1.2",
        sha256="dcc092608635e66216174810d448c750f0cca93112ae62675a4077dd9f0be25f",
    )
    version(
        "2.1.1",
        sha256="1b4365489a687f8e90f44e2b36d97746898802d96f43476a723cdb80c12a3e25",
    )
    version(
        "2.0.1",
        sha256="2ffc1139b2d886210ff8290bf8cdfa24b3688b2f1cd9ae239b476b3bafa60473",
    )
    version(
        "2.0.0",
        sha256="a24888b330fdbb02e963d8490b3b1eb53b4069745c37cb0b5c444aace23cffc6",
    )
    version(
        "1.1.7",
        sha256="05beeaf35ba65317cbae81c7bdb77901438c65d5552b2862fad04494e1f26aee",
    )
    version(
        "1.1.3",
        sha256="cccbdf6cc21a2c597edeea59ecc5b677dcd139afb423d59289696aa20bf351b8",
    )
    version(
        "1.1.2",
        sha256="04a1676d731a8b74dbf4339f963f0a72b9b033ec7da03dc9192d06d4325429c4",
    )
    version(
        "1.1.0",
        sha256="e596c5c7a291d426fb1baef16511ac515b7713cfd5f690cc887235e49677c5d6",
    )
    version(
        "1.0.3",
        sha256="cbe6c639c7b6b5d7256a7c5c90c8aa62d38f0723d719a743ddaf872c7f184408",
    )

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-hdpx@1.0.5:", type=("build", "run"))
    depends_on("r-icams@2.2.4:", type=("build", "run"))
    depends_on("r-msigtools", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-cosmicsig", type=("build", "run"))
