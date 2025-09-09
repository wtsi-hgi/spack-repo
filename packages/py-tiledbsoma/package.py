# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTiledbsoma(PythonPackage):
    """Python API for efficient storage and retrieval of single-cell data using TileDB."""

    homepage = "https://github.com/single-cell-data/TileDB-SOMA/tree/main/apis/python"
    pypi = "tiledbsoma/tiledbsoma-1.4.3.tar.gz"

    version("1.17.1", sha256="85c4a6e3120b0f41e1506472dcc6cc3f05c0273d94808c74fe22b7b522cf6865")
    version("1.17.0rc0", sha256="6dccdf248aaeaf0cb4840f6b1bd9eb4cf35c8b07c4bd585ed951065cce90f476")
    version("1.17.0", sha256="4297f5ca42d23f3361850ffbad0e54e7d0c3713c2a939de1b9aa2ee257bc8c7b")
    version("1.16.2rc2", sha256="18462d90a15ab994b3138d2e39dcdd694ab78d757af3381dc515b15f6ecd8422")
    version("1.16.2rc1", sha256="b388594bf92be691dfd2ff84c958dde6bf4dd5a280f224f4f3a1877f8032afed")
    version("1.16.2rc0", sha256="c7b48c5c48b30a33955cc8e55e21dcba46dc667700bd6bd35c1510542d9c649e")
    version("1.16.2", sha256="c4b366c18daac8e460ed899c75e7cbfca789c07af6d8268b9c75bcb942755ab8")
    version("1.16.1", sha256="cdc5d50c98ba990f2abfe352a88d35ece8700ae2c57af44c1aee67853e299b24")
    version("1.16.0rc0", sha256="294848190bd6cc59b731555983346d32866a6c99ee8ea4c3405fc247fa733904")
    version("1.16.0", sha256="ae25894fc1cb53a2d21e44bce9008b5439b0087850795782d04044d278d5e87c")
    version("1.15.7", sha256="b7617ae3085cb78a4dd6c46df1c7ab6f1af95dc1a483f0970ebf7905b43dcc46")
    version("1.15.6", sha256="1170299c8733c9f38762d5cfdddd8114224a6c2dbcf7c1ec5f17a4d47941271b")
    version("1.15.5", sha256="4650a275dac07ffd51264de36fb7315a03ed0e4507d2932769e1c522b5d89839")
    version("1.15.4", sha256="aaf30fffb3843b99e6b4ecd093b210107c1438b69edfce7d8dccfbf44445e82c")
    version("1.15.3", sha256="cdbc8515c87a4833b51682e57d32ac8afe918165d7474bc05c6e19fadb8140f3")
    version("1.15.2", sha256="c494d6ffbfe6f8cf5e10e61d154eebe73b8e9fa6c00fa93163052178d8a8bed0")
    version("1.15.1", sha256="689bac17d8366bea25f9de3d09ea6f5b4194bde81cd6d8caa6e554b3cac79b98")
    version("1.15.0rc4", sha256="49f30a6c07c9e3a8e7b5b921688de4167e1a7528dadbb973995d32709e532983")
    version("1.15.0rc3", sha256="bf9275bb903674865f3a047c3643a62bb5f1472ea9cdb69dac4ae5ec720f2f68")
    version("1.15.0rc2", sha256="67112eb1e8c5796975a63ad238368a6d8d1fd6e34b084c785a7111b262c701c4")
    version("1.15.0rc1", sha256="a6a79114601ddfa4d10730e75e04b9fec4578a01987964b169115fa4cca457bf")
    version("1.15.0rc0", sha256="9499ac78554040cb817f5cb1595462fbffd5592bbbc45a55edbc0a33ccc5d76c")
    version("1.15.0", sha256="6d835994170db174745f35b86f833d454aa05df07ca5668b41b08d2170e44922")
    version("1.14.5", sha256="77a54647d2c8329b84a88303e915229dff81a62ecb46bd6d84cb931ca45d94ff")
    version("1.14.4", sha256="af7b8fb7302e66ecbfdf3d0e3d35cdd6c6ebaabe54fcd98f9021466d855a3bae")
    version("1.14.3", sha256="806a1e1280f0117f3f954c6521e6cc06dd24d2775aa887c0cf7d21823498ecf7")
    version("1.14.2rc0", sha256="e750018b0f97366d20aa0f6539e29198462c16cecd10d03dd06e8dd453cae3b3")
    version("1.14.2", sha256="a452abbd6f54da9f2aecbb95c9b8dc0f7029391f46773e669595b3f74e26ebfa")
    version("1.14.1", sha256="2cf0b0b3ccf9e1b80df1baf41f133db7c8433e413ef7c0791e00df8ac5d978f2")
    version("1.14.0", sha256="fa3ecfe0d9b80e32fc260b7fc1d85fe632a7c8071f6dcba2fc9b90ba8925fc53")
    version("1.13.1", sha256="14db76fb643e22c267645b7d9cf59a4495d6b9372da543a9322c341bcd142da0")
    version("1.13.0", sha256="274805f93ae3276a9c3bfd2f085fec3da4361479a9b6ed4f7c32a4c880ac71cd")
    version("1.12.3", sha256="6c9a1e0ada17793e68160ff4f1f4cdde26a385ce5d8309992e64fd52a9a6222f")
    version("1.12.2", sha256="673ca4e0e3060006f68548bcc7e10d836950b5ec889749de4a4f6a526a4727b6")
    version("1.12.1", sha256="651e0b7605c19196d0ff4cba282ad09bc767fcd131bba89557c30da1f80a5d6a")
    version("1.12.0", sha256="8e0e510ce7d9b6d4e5697262491ae770183103f27e3fb652ef188ecdb650f4d1")
    version("1.11.4", sha256="514722286534fc76d37471e60eaae8c6b399abd99a4223624e8a36e2910f577d")
    version("1.10.2", sha256="1aa1285df7b2dc3bcac3bd57ae1cf8cd9f3740fe2daa69661ddc9d169d143534")
    version("1.9.5", sha256="f9706ba6a51f820b03b2afdd8737c0c937805ae10ad0d15f407f6a80cc3a5649")
    version("1.8.1", sha256="6088c589c769cdb3a97002744f71239c28c26c1507d74efbef76403d370a1d42")
    version("1.7.3", sha256="f9444f75a0d5499e6ec5576d86c40f77bde9de56d24463626d7fa19d34a9c04d")
    version("1.6.2", sha256="085e7882c1b0a652fd466ee9842160002dcf4aad7e7be7f50d3dad063f3e6b70")
    version("1.5.3", sha256="cef3d03f667ba6b806c19a76acb53619546aed1a70d4a604f9bc045c83731cbd")
    version("1.4.4", sha256="6a22d17b4769b00c5a3431307488c92fd81aa693c20a998938d57326dae8fa01")
    version("1.4.3", sha256="4f137efd06281b90e673526d55cd4ac2141c3f3f782735b1084fc3fd6b2c2bc5")
    version("1.3.0", sha256="42ec45a1743ddd62920686169489b207be92c31fda5d82ca5c4833ff60744283")
    version("1.2.5", sha256="657a60be3cda0daa6657b9a8a4e14a7732ab0166311cbc2cc32e8047225e8d3b")
    version("1.1.1", sha256="7472423c16fc0459f0d9fd62f405bbe2985222f80008be6d50d6b5261076f4fd")
    version("1.0.1", sha256="4902eb1b47890e1e9e113b87d323cd52706b58074c34a5fe9de20ef1c0fd1320")
    version("1.0.0", sha256="6f7fe81765b2376ca88142f5b7c1b316ae11b319959b3d0e8067fcc94338a0ce")
    version("0.1.20", sha256="2b635ae5f65a428a4e66f9e5c24629009beef92d6181dd2b8e551c833f05e1b2")

    def patch(self):
        filter_file(
            'import setuptools.command.bdist_wheel',
            'from wheel.bdist_wheel import bdist_wheel',
            'setup.py'
        )
        filter_file(
            'setuptools.command.bdist_wheel.bdist_wheel',
            'bdist_wheel',
            'setup.py'
        )

    depends_on("py-wheel@0.37.1:", type="build")
    depends_on("py-setuptools@65.5.1:", type="build")
    depends_on("cmake@3.21:", type="build")
    depends_on("py-typeguard@:3.0", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tiledb", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))
    depends_on("py-somacore@1.0.28:", type=("build", "run"))
    depends_on("py-shapely", type=("build", "run"))

