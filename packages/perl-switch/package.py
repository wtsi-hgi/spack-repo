# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSwitch(PerlPackage):
    """A switch statement for Perl"""

    homepage = "https://metacpan.org/pod/Switch"
    url = "https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Switch-2.17.tar.gz"

    version("2.17", sha256="31354975140fe6235ac130a109496491ad33dd42f9c62189e23f49f75f936d75")

    depends_on("perl-module-build", type="build")
