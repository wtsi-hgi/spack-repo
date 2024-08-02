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
#     spack install perl-irods-wrap
#
# You can edit this file again by typing:
#
#     spack edit perl-irods-wrap
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlIrodsWrap(PerlPackage):
    """Perl iRODS Client Wrapper Library."""

    homepage = "https://github.com/wtsi-npg/perl-irods-wrap"
    url = "https://github.com/wtsi-npg/perl-irods-wrap/archive/refs/tags/3.23.0.tar.gz"

    version("3.23.0", sha256="88a54af6d53b5ceb3b4bb217121fc0f8be66e60986977257da154a288977f7d1")
    version("3.5.1", sha256="3af819f67b55501c870449ceb588aa02bcdaf83b9f118bfe384a761176e7c56f")
    version("3.4.0", sha256="e5f9ed9698ce7c01797db8a16a8534abbffd96730478e282b41be2fa86fe1047")
    version("3.3.0", sha256="54331858820998f8618f600f8fa37eedcae8ede8d98c7a72269632557555158b")
    version("3.2.0", sha256="d9089026eba91d8018ad9cc847e72468059f39eefdd1a32b984847a32dc5fb9d")
    version("3.1.0", sha256="8437fc0aeb871d15b121b88f51970919d76f5e0b847affd3ac89c634302ccadb")
    version("3.0.2", sha256="d249bc5b15a89ab9e6ee02c8f66d796996c1b0ed1b2f8fa3b007404bfa8adde2")
    version("3.0.1", sha256="21ff8768c7f52ff3324862af824f217cac7dab0ce1f9b190df898f8c3f7cd1dc")
    version("2.8.1", sha256="6768b258909a4fe6503f111c3e2049f3b32d53932366967d5aea44daf8166fae")
    version("2.8.0", sha256="c3a671d52ac111db4669b13819cba3d98959ebfe5f3622bab2143a1f2db19914")
    version("2.7.1", sha256="4f686d8f55a597f7ad441e53d6210ec12998fd0b7ca512a5b4013a95f047c750")

    depends_on("perl-module-build", type="build")
    depends_on("perl-dnap-utilities", type=("build", "run"))
    depends_on("perl-namespace-autoclean", type=("build", "run"))
    depends_on("perl-list-moreutils", type=("build", "run"))
    depends_on("perl-log-log4perl", type=("build", "run"))
    depends_on("perl-cache-lru", type=("build", "run"))
    depends_on("perl-datetime", type=("build", "run"))
    depends_on("perl-data-dump", type=("build", "run"))
    depends_on("perl-moose", type=("build", "run"))
    depends_on("perl-moosex-strictconstructor", type=("build", "run"))
    depends_on("perl-set-scalar", type=("build", "run"))
    depends_on("perl-moosex-types", type=("build", "run"))
