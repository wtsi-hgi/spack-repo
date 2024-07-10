# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoracle(RPackage):
    """OCI Based Oracle Database Interface for R

         Oracle Database interface (DBI) driver for R.
    This is a DBI-compliant Oracle driver based on the OCI.
    """

    homepage = "http://www.oracle.com"
    cran = "ROracle"

    version("1.3-1.1", md5="01b528d46985dcf3888fae41b2f08c8a")

    depends_on("r-dbi@0.2.5:", type=("build", "run"))
    depends_on("oracle-instant-client", type=("build", "link", "run"))

    def configure_args(self):
        return [
            "--with-oci-lib={}".format(self.spec["oracle-instant-client"].prefix.lib),
            "--with-oci-inc={}".format(self.spec["oracle-instant-client"].prefix.include),
        ]
