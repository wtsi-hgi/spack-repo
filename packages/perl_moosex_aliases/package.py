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
#     spack install perl-moosex-aliases
#
# You can edit this file again by typing:
#
#     spack edit perl-moosex-aliases
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMoosexAliases(PerlPackage):
    """easy aliasing of methods and attributes in Moose."""

    homepage = "https://metacpan.org/pod/MooseX::Aliases"
    url = "https://cpan.metacpan.org/authors/id/D/DO/DOY/MooseX-Aliases-0.11.tar.gz"

    version("0.11", sha256="c4850f972426c3447aaeed8dcb4033e84460ca51705ad3ea78b63af919fe0748")
    version("0.10", sha256="9fb293e6eaaadee8874fcda168a8d4e6517631c1c1be631513549f66ba017fd8")
    version("0.09", sha256="720d96e5640a57df6a7c613518efb187686739a4ad902044d7197525c617ce07")
    version("0.08", sha256="00727df3a63e44d2e9635508f77eab49c91efd0f617d4c682f709737ec049440")
    version("0.07", sha256="1afa9d6531f58a338132c528647c34d97b18f0db5bb6822dec07e88ec4bba09a")
    version("0.06", sha256="804e74967ef2a5b62e02c010d473e19f30a63a0d8ed56ba424b9412d38b10993")
    version("0.05", sha256="763fda8a5df896b93a7834cc20623a6fb0771058d78bcdd9bc82c3fea0fd7cea")
    version("0.04", sha256="3c91e53cb5c1d6f42097b3662ccde80a3f0d956d01cee5c6e39b08227aaf968c")
    version("0.03", sha256="62e6b07035832f33540324bb343b26f2f2d5b22b1a83ba71aff7e1be17dca056")
    version("0.02", sha256="14cd3373caa6db4368dd902c5e2cea9c18e3330fb087cc255fd3b8d73c29599f")
    version("0.01", sha256="f1b6340cd75449d77f4c3c3a04421f1fd51ca1f6cc73decdf667cfe15bc5fdd1")
