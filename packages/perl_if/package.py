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
#     spack install perl-if
#
# You can edit this file again by typing:
#
#     spack edit perl-if
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlIf(PerlPackage):
    """Use a Perl module if a condition holds"""

    homepage = "https://metacpan.org/pod/if"
    url = "https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/if-0.0608.tar.gz"

    version("0.0608", sha256="37206e10919c4d99273020008a3581bf0947d364e859b8966521c3145b4b3700")
