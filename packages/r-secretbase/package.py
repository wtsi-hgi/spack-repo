# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecretbase(RPackage):
    """Cryptographic Hash and Extendable-Output Functions

    SHA-256, SHA-3 cryptographic hash and SHAKE256 extendable-output
    functions (XOF). The SHA-3 Secure Hash Standard was published by the
    National Institute of Standards and Technology (NIST) in 2015 at
    <doi:10.6028/NIST.FIPS.202>. The SHA-256 Secure Hash Standard was published
    by NIST in 2002 at
    <https://csrc.nist.gov/publications/fips/fips180-2/fips180-2.pdf>. Fast and
    memory-efficient implementation using the core algorithms from 'Mbed TLS'
    under the Trusted Firmware Project
    <https://www.trustedfirmware.org/projects/mbed-tls/>.
    """

    homepage = "https://shikokuchuo.net/secretbase/"
    cran = "secretbase"

    version("1.0.5", sha256="5a8d54c07c4e2a12b50d06dcfd20d778f307d8418cd3aae390b04f0d546bb091")
    version("1.0.4", sha256="e86fdef5a57ac6b00669092ede5ac26dad27b03e19c1f72bd79128019c68c7a6")
    version("1.0.3", sha256="c6aece3ffd0aaefb737d8d66f27495465ed40b485edee44e32fa2ccead5cb62e")
    version("1.0.2", sha256="89bb33b7d49056f6e31ae56748caff34867eb5cd3f77e420c6cbf979c9e5d444")
    version("1.0.1", sha256="abb9c06abb8e0657a54786aad104de336991c3e2795226bce225bba7374d6e04")
    version("1.0.0", sha256="90a34d65ef476b839508e29fb188d2abf49eed76b29086476b8f69c3ef9dd5d2")
    version("0.5.0", sha256="e42d5f5d50717e22bec97e072f8dcee08c267c5af990a2eeebf1d2b4c897bd13")
    version("0.3.0.1", md5="e6f9c238f463c7b4f850e18988167972")
    version("0.3.0", md5="87d9c1c967bcbdcdf4c6db3541bc905d")

    depends_on("r@3.5:", type=("build", "run"))
