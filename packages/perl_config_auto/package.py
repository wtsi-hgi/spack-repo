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
#     spack install perl-config-auto
#
# You can edit this file again by typing:
#
#     spack edit perl-config-auto
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlConfigAuto(PerlPackage):
    """Magical config file parser."""

    homepage = "https://metacpan.org/pod/Config::Auto"
    url = "https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Config-Auto-0.44.tar.gz"

    version("0.44", sha256="e960e04df995852aba275cf83ac6f947e44a4139de156858c01f0cec7f7ab53f")
    version("0.42", sha256="d038da0eb8835c8d38a7c1bbe8b200545e5a91915407a10a17eef460a7fbac10")
    version("0.40", sha256="4411a6a962028982724d1f3f3b58c9515102d49c4e62bab2a853122a7acba59b")
    version("0.38", sha256="d283e336b1598c666e241ae2d57bb5f8ee05f60720359a0b2f5808dfc50d462c")
    version("0.36", sha256="be4ab899c8d77a491344ea30409765397ccac11999c97044bdb6210d31480967")
    version("0.34", sha256="57580b8d5bbb4a6beb08d469fb966cc18144e69b8fa63cc4e7d14c095bd539d4")
    version("0.32", sha256="3a949df65e350d0fcb66839fc31d52823820a5b3845e5615d5fda2409941230a")
    version("0.30", sha256="e035fca67db2d2be5125ea9c30232ce3ee7b30f88bc0306b01d5cc95f89a7c2f")
