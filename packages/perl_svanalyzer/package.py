# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PerlSvanalyzer(PerlPackage):
    """Just as it does for small insertions and deletions, sequence similarity at the boundaries of large insertions and deletions can make the precise specification of boundaries and allele sequences ambiguous."""

    homepage = "http://svanalyzer.readthedocs.io/"
    url = "https://github.com/nhansen/SVanalyzer/archive/refs/tags/v0.36.tar.gz"

    version("0.36", sha256="ca587eef1882fb76cf9880143e2246063cac6691d211b39958e7b1c0a3a92fec")
    version("0.35", sha256="a6e6f11b300ab05b67013d25db2735830c90ef56037fd73e5604b92cab8ef75a")
    version("0.34", sha256="826839eb379cb56a263108d5452fff9a7c72d07cca2bd03ee8c39a8d52a714d2")
    version("0.33", sha256="9f03b54cbc34c95c0c16bd748360ef06952d24eca4a0a75c76963d4b632ce750")
    version("0.32", sha256="d562145f61af609d608668ff0f62227c10b61994bafbfa9f5e2bee763de85e05")
    version("0.31", sha256="e96288a8be1e865a42d35560eabc17ed56d5535365d662cddd65258ad8ab234c")
    version("0.24", sha256="264abc4f6058ae0a2fce5c41a14b562f6756519e115f3c468a898ea3dfdaa36d")
    version("0.21", sha256="825204785c3aaee76b5f0b70969fd816507564592380356b46ba8c6901cff5a1")
    version("0.3", sha256="7a2d324c81c9bb53d2db15bbd4800ffa542e805a33b10ea7cae6316870ec1645")
    version("0.2", sha256="46a34c3418b1e7c91b9cb87da2ca8a8c8d2b3e1d0e542d1e56b69241190dac36")

    depends_on("perl-module-build", type="build")
    depends_on("htslib")
    depends_on("edlib")
    depends_on("mummer4")
    depends_on("bedtools2")
