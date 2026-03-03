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
#     spack install perl-test-deep-json
#
# You can edit this file again by typing:
#
#     spack edit perl-test-deep-json
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlTestDeepJson(PerlPackage):
    """Compare JSON with Test::Deep."""

    homepage = "https://metacpan.org/pod/Test::Deep::JSON"
    url = "https://cpan.metacpan.org/authors/id/M/MO/MOTEMEN/Test-Deep-JSON-0.05.tar.gz"

    version("0.05", sha256="aec8571b9e31b7301e26132c132c6800952dc089c645d76954a3ad1a6b350858")
    version("0.04", sha256="8e3dc188bbf930254cc9b24ae569b21c14fea71b977f387a3c6a9859b8c13fab")
    version("0.03", sha256="41bef600487d56b0e075ca34e78297b2bc035304fc525e2e21ab735c650f48e1")
    version("0.02", sha256="a7e277e4c40945474f815c367c0acd799c2430b4f37041c3469335d10afe3d65")
    version("0.01", sha256="eb41affb1d4cd95defff4dbba3687c841b55efff68555a8e07ca2e151081b558")

    depends_on("perl-module-build-tiny", type="build")
