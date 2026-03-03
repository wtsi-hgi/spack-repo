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
#     spack install r-multinom-rob
#
# You can edit this file again by typing:
#
#     spack edit r-multinom-rob
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RMultinomRob(RPackage):
    """MNL and overdispersed multinomial regression using robust (LQD and tanh) estimation."""

    homepage = "https://rdrr.io/cran/multinomRob/man/multinomRob.html"
    cran = "multinomRob"

    license("GPL-2")

    version("1.8-6.1", sha256="46a71e352438762e897925f14099f6cd48bfa814edc2cfe4f12e1d75ce74b2b9")
    version("1.8-6", sha256="7f0253600852eba3b3c9e44a762628e29426753acbae46ceed628c3cbe698308")
    version("1.8-4", sha256="9598de2215826326352f31ff50c5147fe18c11040e2670bd86ed79253fb16b3a")
    version("1.8-2", sha256="537bf5d12f6965b395ab3f0ab7974f89f93116262aeb7af5e44f9f22f08fb1ab")
    version("1.6", sha256="6d589d9e16456b9e64b093a524f1cd9818ff4fb5bf3da2dc3b4dee5536c6e12a")
    version("1.3", sha256="a221f8e384d96ae72fcb6a5b4429f2ae737532429bd702f17bd82fdcb4205607")
    version("1.2", sha256="e70cf1076eeee1b6d33dcb93405c53c7ba64aead8b52c1bdc6caa12e8b69f4a0")
    version("1.1", sha256="93dfb52bad8442870f52d1822ff69e57734b6bc7f068fd63438eafd9ed3ad060")
    version("1.0", sha256="d6759a91876033092fe565ee8aa6adeb5ff39aca988000bcd3550adc2255dba4")

    depends_on("r-rgenoud", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
