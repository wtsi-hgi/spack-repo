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
#     spack install perl-list-utilsby
#
# You can edit this file again by typing:
#
#     spack edit perl-list-utilsby
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlListUtilsby(PerlPackage):
    """higher-order list utility functions"""

    homepage = "https://metacpan.org/pod/List::UtilsBy"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PEVANS/List-UtilsBy-0.12.tar.gz"

    version("0.12", sha256="fff1281fd469fe982b1a58044becfd970f313bff3a26e1c7b2b3f4c0a5ed71e0")
    version("0.11", sha256="faddf43b4bc21db8e4c0e89a26e5f23fe626cde3491ec651b6aa338627f5775a")
    version("0.10", sha256="bed74094c625aa34a5ae94a7e1fe1856f08e1bd26b8ba152bfe7a51d3277192e")
    version("0.09", sha256="41e52a159af343af5b529ba17fb04d5ea861dd57a8615e3f3806a284d07f9af5")
    version("0.08", sha256="ca0875e454d709277c70acffbd5cc9a045c1f2e6b09192ea528c5d6dc35a0d9e")
    version("0.07", sha256="adfc21cbcf646f7f7d02f77c344245098d95b140aa14301c9e47fc4fdd8194ab")
    version("0.06", sha256="c7a24e898cc8559140706d6756113959026ca88972d06906976869bfef16e3c7")
    version("0.05", sha256="af183f5e60dfe92bd1d11e88763ea6ed1236675456749f5910789d47413e55c1")
    version("0.04", sha256="c4e8ce15c669d2d9c2439eab861c8f441eae5405ed6b6865cb48321b8c0ffc64")
    version("0.03", sha256="7de0f77baf0eb1a8f3dc899437e24c9d594db497af79ea508ea898cd48ba7be9")
    version("0.02", sha256="07fbc24c04e66ec899f303cd99c22011cdd8ac08fe3bf1f5a350304f68ffc96e")
    version("0.01", sha256="3ad41ae1c90958c136f19b1e36b6f76e0acf4d4a6632ca2bd39c9fb82c3cafbd")

    depends_on("perl-module-build", type="build")
