# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLiftover(PythonPackage):
    """Package for converting between genome build coordinates"""

    homepage = "https://github.com/jeremymcrae/liftover"
    pypi = "liftover/liftover-1.3.3.tar.gz"

    version("1.0.1", sha256="3ec635b08873014c83873075d82c5594f82a6493d206c46787a9795599468c5e")
    version("1.0.2", sha256="1ed80a997e3a12c6a38c4b9ca311fc3c3a828a4f4c6fa99e90a578022e039021")
    version("1.1.10", sha256="529e373478eec1cc339d28292a10aad4c488a8f66d451853316b42d1c9c24e5a")
    version("1.1.11", sha256="588e50c010cb905c2ec46853cbecf9fc2eb8ee3f2a74cbc28fcb3a7ce3b8a0a5")
    version("1.1.13", sha256="21582ae545fa343d8942dd7b9f582364554790d703033ab8675a268345faab9a")
    version("1.1.14", sha256="d2a4a4178812acfd9339e7c96dd75e4ccbc7480119649ef3cc96263a567bcbc2")
    version("1.1.15", sha256="b95cbf8dbda5fe867f8ca104f5110d0a139b7b78b53fd372b987f01a160ae743")
    version("1.1.16", sha256="fc1c92ef3279b61a2ccfd8c3cdb9cb4829b11a0f9356d15097c611fc0064fd0f")
    version("1.1.17", sha256="cb06a3843b570ec554fbc0dd871c0b87d3645200e2c65f6cc97cd4b6146efaf9")
    version("1.1.18", sha256="a4bf896c5dd59a284929d68f446a78c426827efbec430d35da1ec7bcd29eac44")
    version("1.1.2", sha256="d91e782d391f0f8c9678e30c5af5a59373f96aead40a2dc422dcd05e6720f94f")
    version("1.1.3", sha256="515d5b117b34fa28d5819bab9b31e7d53651d489b37d36a59cbdabd7e2cf70e0")
    version("1.1.4", sha256="1218c540bdec06c0ae5b3a2f4703020d388ff85f53bb91f8a41efa1bf3352f68")
    version("1.1.5", sha256="df1f566b4670413dfbcd1185835dc7b6a5544ca5cddd81b43820bad59d204a88")
    version("1.1.6", sha256="c2c1f80de1d21a6969ebeab49693d1955cfb09fe17dd1f5749367c6c9ce6fa1b")
    version("1.1.8", sha256="9bf935d6ef9ef378f7b58d134b39a4ebb3d91ba0a003b756b27ffe2b2827c592")
    version("1.1.9", sha256="12c7d919a8d8d3691eda528c37b0dab1fb5dc89c54a5defd9a9dfe75a55129c1")
    version("1.2.0", sha256="3b9fc333e8627c5f0117771c0a452163c1ac7d2ff3732d9d1f9010a833fce955")
    version("1.2.1", sha256="43d89d929288b0f2031f6200958a920d6ec71a0929a91abcfd73b15032f20116")
    version("1.2.2", sha256="f858aed016227882263d369969790adf6df2c07399e16f063aec8a248a2b4513")
    version("1.3.0", sha256="72b870e47a14210ff3bb6c14d90087b348149765780c65a7699a3a56f7ae7016")
    version("1.3.1", sha256="43173ba201f2ad2ffd84c699b228d3f21da58e4d087d15d8bdcf600697ade10c")
    version("1.3.2", sha256="38ca61efcbae850058735649230fd2dc68e69b8a3fd5d67b637aa61c37b77eea")
    version("1.3.3", sha256="4d6b3bf69d8fb5aff4b817f78eadea263ddbafaa53242436604e795a68691152")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-urllib3", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import liftover")
