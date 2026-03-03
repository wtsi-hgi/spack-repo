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
#     spack install perl-sub-exporter-formethods
#
# You can edit this file again by typing:
#
#     spack edit perl-sub-exporter-formethods
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlSubExporterFormethods(PerlPackage):
    """helper routines for using Sub::Exporter to build methods."""

    homepage = "https://metacpan.org/pod/Sub::Exporter::ForMethods"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-ForMethods-0.100055.tar.gz"

    version("0.100055", sha256="791f4203ba7c0f7d8380bc01bec20215f7c8bc70d7ed03e552eee44541abe94e")
    version("0.100054", sha256="eef61c9421688bb3a7beaca71623df11c8a749307ae428abdabc556e2bfafc3e")
    version("0.100053-TRIAL", sha256="59db80f8b5c0c42c586b055ae57bf125b6c0e07d3864f04a48a8aac7e7a5f385")
    version("0.100052", sha256="421fbba4f6ffcf13c4335f2c20630d709e6fa659c07545d094dbc5a558ad3006")
    version("0.100051", sha256="f5c61eb5cd0f4472aea1f270c2a1ad2fece1e965f1ab2df2b9f7dc5178b4fc88")
    version("0.100050", sha256="67dfaa39c58995ed1d341d7f2e785a68b7ba4ade72608f491459b8d2dee6df33")
    version("0.091970", sha256="a86df830a6d4697e4ce6d571e6d622abc3739b2b812ec8ea1a7d1ecb1b38535b")
    version("0.091810", sha256="4a11c258ee082e5cc261eb7e38c1878d0356f371d28f05908f2f2c59401f20c6")
