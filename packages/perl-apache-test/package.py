# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlApacheTest(PerlPackage):
    """Apache::Test - Test.pm wrapper with helpers for testing Apache"""

    homepage = "https://metacpan.org/pod/Apache::Test"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHAY/Apache-Test-1.43.tar.gz"

    version("1.43", sha256="a9999f02a781a589218b589b1879c11c495a745af09575e5cbb22dfcb65680ac")
    version("1.42", sha256="0681f07d7d8a9429d0edf8a8c5ad6a655be7fe81ada142670b2b8e776b3bb3eb")
    version("1.41", sha256="38cf60b9d63156a8043b8fc75b1b41132fa35228910e61089e08bb84869ab018")
    version("1.40", sha256="3cf537f1c81deb549d62be7fd5ee1af439283a9e93f3d13465d01a1d41d4ae40")
    version("1.39", sha256="d8543864ff29e8ac3d4004c5c7014b1fe490b2024104ac4c24683a74bba62089")

