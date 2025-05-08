# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlUri(PerlPackage):
    """Uniform Resource Identifiers (absolute and relative)

    This module implements the URI class. Objects of this class represent
    Uniform Resource Identifier references as specified in RFC 2396 (and
    updated by RFC 2732). A Uniform Resource Identifier is a compact
    string of characters that identifies an abstract or physical resource.
    This includes the URI::Escape module for percent-encoding and
    percent-decoding of unsafe characters in URIs."""

    homepage = "https://metacpan.org/pod/URI"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.31.tar.gz"

    maintainers("EbiArnie")

    license("perl_5")

    version("5.31", sha256="b9c4d58b2614b8611ae03a95a6d60ed996f4b311ef3cd5a937b92f1825ecc564")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))
