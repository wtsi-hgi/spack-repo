# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVlConvertPython(PythonPackage):
    """Convert Vega-Lite chart specifications to SVG, PNG, or Vega"""

    homepage = "https://github.com/jonmmease/vl-convert"
    pypi = "vl-convert-python/vl_convert_python-1.8.0.tar.gz"

    version("0.0.1", sha256="cc6d922b734e25bc8a314c0c01d7744c35d87ed3095a6377299b65a2b79fd946")
    version("0.1.0", sha256="92875d9ca02d1b7683cde9a92c5a910bb7406c013d38fdf8564ffd69907a4529")
    version("0.10.0", sha256="15ab1068eb9457bd9d344a0cc046594a7ee7bb02d1c38f80972d329254960877")
    version("0.10.1", sha256="09aa98a8c5b59551c8d3a95bf657b48e1e7e90372532bcf1479c35f470c72cf4")
    version("0.10.2", sha256="232212e89ad04303766d36dc1cc93a6925424480b0a787ca55ff3360199f3775")
    version("0.10.3", sha256="bcfb015a6834c4a86bd126ef80c4fe6abb8609da798915fe1683532ae40b5d80")
    version("0.11.0", sha256="660605a272f7bf35ebc45368429b4bd9bf650da95162aaf9f1d70797e09d8a7b")
    version("0.11.1", sha256="0c7e9b0331fa6d2128a5129e4afcf6bbf2b87e665216f3df242ed5d43c28bcef")
    version("0.11.2", sha256="3e2db75b9236f1f828e38011ae05c7ad6c25fddc42eec70e5bc1cd2e7b7f6bdc")
    version("0.12.0", sha256="a2279a6a4b8e5aefa713ecc1f999d684656a6e37fca1c25114c66def3e867f14")
    version("0.13.0", sha256="8fda3ef10b1c2268f0d504e3860808785c8362b5eb6a582272882726decec899")
    version("0.13.1", sha256="d70a608257dd6b5b782d96cccebfe7289992e522e47a8bebb7d928253ca8b396")
    version("0.14.0", sha256="8d3d63d7c8e446cb2e9bf2209513b3c608805152acdf50275a6f430fa18d6613")
    version("0.2.0", sha256="92df145b8f232962d22141234630054ba05d7066b2ca262d0f10c671728b9b0b")
    version("0.3.0", sha256="2a76ac70d2ef9ad772602a9559f453d95fa9297facefabdbbfaca86372522f6d")
    version("0.3.1", sha256="01c8ae5edd66bbcf097437a2bcb1c7be7aeb262a3c55648cfabcf666c26a3850")
    version("0.3.2", sha256="a0b0827827d727a4c8d9a2989d5cfd11ba52cb9f0ff450a0dd6df33326922662")
    version("0.4.0", sha256="12d56ff4b137e058b6f8e1ada9b06609b109c084c7060b2d1b0548ffac1898d6")
    version("0.5.0", sha256="2fa22e59c5773d48d9db8932b545c3ec3c5ea10414e48eb003aedff57208bdfc")
    version("0.6.0", sha256="f1c7cb9b9071712519c19b26e0815709b782d97ae3cb6953e240a91b708a01e1")
    version("0.7.0", sha256="66f91687317bb9c4b21c1485ab9f51bd122d07ee741e24718432e9cff1226516")
    version("0.8.0", sha256="490bad48447cfdf9e88fc8197b90f02744cbb8236886385f9d17fb1d9fc8b4e6")
    version("0.8.1", sha256="80ab07aaa4f2df120537747152d18581d9e27760ed14769a3c09466fa5c2f07d")
    version("0.9.0", sha256="ca1b9c2de1ccb7316331eea08c13aaaea03a752c04c3c14878f88f738b826cf8")
    version("1.0.0", sha256="3e776a8c7d7297b078830ff56a46754aaf5c139a78b4aaa5bbc13bc6f6a87c31")
    version("1.0.1", sha256="488565b6a0eb5e75558f82147217c5090672bee58745e79225b2f2902db9fffd")
    version("1.0.1rc1", sha256="824ac71cffa31718c7cad8f307359d1fdce6d215ef3e71f16b57acab6f98cf02")
    version("1.1.0", sha256="cc2bf58e019a5b4796b2903af8eb952555a7701603e0752e9f9fe66627af5c2e")
    version("1.2.0", sha256="fa92eba4c84cb69aa88c10b70e03de75318394ce90ffde1a657c644563380ed9")
    version("1.2.1", sha256="8cde0690434b6ece26df0206bb7dfc76c9b3cea73d7085a1ced59ccb3526a1c6")
    version("1.2.2", sha256="dbb93e1b0b8dbc8535bc0cf07d5ff2e61de6ee7b3ca435aab6652d5c09fe6e64")
    version("1.2.3", sha256="1adeaa46041ccff47fee0119b136f5e12211d56726a142fc78cb14ad3c141e09")
    version("1.2.4", sha256="d6f2794532752a1fe142abd578846b95cceee3e3abe228764760c6ef7bc4a320")
    version("1.3.0", sha256="de1462151dfbba7b2a17881dac1d2269662012c252f1e9d1537a4daed5e36067")
    version("1.4.0", sha256="264d6f2338c7d3474e60c6907cca016b880b0c1c9be302bb84abc6690188a7e9")
    version("1.5.0", sha256="ba1e13a84f5a3d1af393d0d32aa19c4268db573d5f5c799bce8a5dc0468b1899")
    version("1.5.1", sha256="014d47361d5f21bbd2f3e3c58455609b9c4ace65f7ccdd881243274f3f91f457")
    version("1.6.0", sha256="f7539c5558026d41d870df3ea92546ef87956c7b62ca99426906e941115bfd41")
    version("1.6.1", sha256="b70935dbf792118a42aae27b7465359cbc014e30e63ef6ba7a0f8974707d9c1c")
    version("1.7.0", sha256="bc9e1f8ca0d8d3b3789c66e37cd6a8cf0a83406427d5143133346c2b5004485b")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-maturin", type="build")
