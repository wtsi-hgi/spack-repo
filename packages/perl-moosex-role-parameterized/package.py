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
#     spack install perl-moosex-role-parameterized
#
# You can edit this file again by typing:
#
#     spack edit perl-moosex-role-parameterized
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMoosexRoleParameterized(PerlPackage):
    """Moose roles with composition parameters."""

    homepage = "https://metacpan.org/pod/MooseX::Role::Parameterized"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-Parameterized-1.11.tar.gz"

    version("1.11", sha256="1cfe766c5d7f0ecab57f733dcca430a2a2acd6b995757141b940ade3692bec9e")
    version("1.10", sha256="4846c12f7cd304419c983eb3654d303462d06a3a5f941e21c76957806c119d5e")
    version("1.09", sha256="b5669b80c4edcd926223b2cb192a846841709ba3db45d75ef9434a08dbbf8c20")
    version("1.08", sha256="58121a8f4edcab823e38241e41d5fdc01c09064c7d09b0bd1121e61170b5428b")
    version("1.07", sha256="d23d8fead86947a187606a42a288706cf0e0f5492872acac7bb3492e8f90811f")
    version("1.04", sha256="ef1415c38ab2e821c1371b138289bedb17cdab39841b9efa8e8955e725c16d39")
    version("1.03", sha256="9c9474f64e53141f11d2b42cc4a1f7558021dbe2d652f584b518f6c6e43310b4")

    depends_on("perl-module-build", type="build")
