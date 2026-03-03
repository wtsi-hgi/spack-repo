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
#     spack install perl-moosex-attributehelpers
#
# You can edit this file again by typing:
#
#     spack edit perl-moosex-attributehelpers
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMoosexAttributehelpers(PerlPackage):
    """(DEPRECATED) Extend your attribute interfaces"""

    homepage = "https://metacpan.org/pod/MooseX::AttributeHelpers"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-AttributeHelpers-0.25.tar.gz"

    version("0.25", sha256="b0c819ec83999b258b248f82059fa5975a0cee365423abbee0efaca5401c5ec6")
    version("0.24", sha256="b891c2ea9bbad10bc6aba4ddd94511c6e8c8eae9395a770090a330ece68613c4")

    depends_on("perl-module-build", type="build")
