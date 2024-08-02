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
#     spack install perl-cache-lru
#
# You can edit this file again by typing:
#
#     spack edit perl-cache-lru
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlCacheLru(PerlPackage):
    """a simple, fast implementation of LRU cache in pure perl."""

    homepage = "https://metacpan.org/pod/Cache::LRU"
    url = "https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Cache-LRU-0.04.tar.gz"

    license("UNKNOWN")

    version("0.04", sha256="1a38d62365ded89315568a80c31f5bf77f1330bf20463ce11a35a6489a6abdc4")
    version("0.03", sha256="7131f08a266274d1c9d3dbac77b610fe69fe1c8589b919833cc0482b1732eae9")
    version("0.02", sha256="0bf6b0fc35e5465149a96ea424569e121cb20fa122505b4d4572d3f79f5c532b")
    version("0.01", sha256="e428f5ba53f2c56448d71f463679f3721c13c30d708f9e0cfc050d3019fbef25")

    depends_on("perl-module-install", type=("build", "run"))
