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
#     spack install perl-list-allutils
#
# You can edit this file again by typing:
#
#     spack edit perl-list-allutils
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlListAllutils(PerlPackage):
    """List::AllUtils - Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package."""

    homepage = "https://metacpan.org/pod/List::AllUtils"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-0.19.tar.gz"

    version("0.19", sha256="30a8146ab21a7787b8c56d5829cf9a7f2b15276d3b3fca07336ac38d3002ffbc")
    version("0.18", sha256="b7c4bf80090b281c4a1560c76a1a819094c3a1294302f77afb8c60ca4862ecf9")
    version("0.17", sha256="1e72d83e752cd31c3d696f660fff05bfeb929e2bdc05613d762396dea02fe619")
    version("0.16", sha256="559b3aa911c73003a3a1ebd860d3b16e171137de8203d86be63a2390364c63dd")
    version("0.15", sha256="3711fac729321d3aad8356a756fd9272094f227aa048866a3751f9d8ea6cc95d")
    version("0.14", sha256="e45aa65927ae1975a000cc2fed14274627fa5e2bd09bab826a5f2c41d17ef6cd")
    version("0.13", sha256="39cf5e114fbc377b513b14be047e27e927b5be68748c193d9ffa766a679d7a23")
    version("0.12", sha256="0b5352317652c22b53bee64e1984efd9f21edfad321b0e5a98cdec5ec87bbcae")
    version("0.11", sha256="762dcb0067fdba061104be834747f6b8bd27897389e77aed458f35dfe4d04998")
    version("0.10", sha256="5c33d562782bd488d2852fe9a8404ac9c765b8d3aa9014c46c55bb15eadf93e1")
    version("0.09", sha256="4cfe6359cc6c9f4ba0d178e223f4b468d3cf7768d645334962f05de069bdaee2")
    version("0.08", sha256="27ddc2f0d47656cd3e08846ffe19f765bbd6c1d0e3c751ce4bb704e2b0b7ad1f")
    version("0.07", sha256="72b52f59ef0f6e79aaaf777b58f7bdf806c71e2f9ea901b5f11c3964536cb434")
    version("0.06", sha256="5a69cfaa32bb150b7c4c50ff01568fd1c0850a560edbb9556bbca9607512a654")
    version("0.05", sha256="111c2faa832f7894d6a811b4e9e130f717f3582dc1f0e6c7546abf7453a10f51")
    version("0.04", sha256="09747e7b93f23d4bcffa5830102bfce473d3779d2adec3db204706ec21bc7a0f")
    version("0.03", sha256="4806cc718c5b7530d0bec48d3f7682e7f55a489be4014519d68f937c11c2a115")
    version("0.02", sha256="5d7e231c80a78f36ea31f1698e0e7abda4ab66858574cebc9fe905aecad073d2")
    version("0.01", sha256="2ae4f7018f3da88c259f5af40d95298e7469bf070eb4bc54b11ed1ba9e332f63")
