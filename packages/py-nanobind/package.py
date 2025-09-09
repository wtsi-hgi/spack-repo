# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNanobind(PythonPackage):
    """nanobind: tiny and efficient C++/Python bindings"""
    
    homepage = "https://github.com/wjakob/nanobind"
    pypi = "nanobind/nanobind-2.8.0-py3-none-any.whl" 

    version("0.0.1", sha256="1e063a64d934990d0d52576c8e2547491c1a787eed785d30bdc465ca37bf3920", expand=False, url="https://files.pythonhosted.org/packages/d4/59/fbbed2634b25e8f365f30d294b522bc556e5cc4bb2b24130ad2931fbcb2e/nanobind-0.0.1-py3-none-any.whl")
    version("0.0.2", sha256="63f3bd185a0d56626dcd0e30fd971a574ab4aacbff4b5e9538d620d441adb23e", expand=False, url="https://files.pythonhosted.org/packages/21/26/26ee638847c62f2b4caaf0dc2cc33e3ec4a7224e24195642c66c909e90f6/nanobind-0.0.2-py3-none-any.whl")
    version("0.0.3", sha256="630299e59aaaf1a5ddb6079134665f4f60742ca95f0b1283f0376be3d9a5c4d1", expand=False, url="https://files.pythonhosted.org/packages/0e/eb/281b9805a81b66f1f28cc066093fb3c6068aa01c80fc7c4ad8761e0d8bf5/nanobind-0.0.3-py3-none-any.whl")
    version("0.0.4", sha256="38a80f5215c8f03b96be38dc351c79aba6a221a6b84db07c867809ea4c06693d", expand=False, url="https://files.pythonhosted.org/packages/92/77/c48cbaf3e2a92864be5c2f5473aff72818d30c4204d3ea98c5ae2ec314f7/nanobind-0.0.4-py3-none-any.whl")
    version("0.0.5", sha256="4b2785fe1aa53fca197bfecc4bfa14da1892bc85cd7729d74b7f111230979d17", expand=False, url="https://files.pythonhosted.org/packages/4a/44/786a8510b0d127487045b7586e55115a492e8eefac58978bbd920b2917e2/nanobind-0.0.5-py3-none-any.whl")
    version("0.0.6", sha256="da6b7ad7cf52ec807e924918d46388ee78a14145dd13f6bf4599f760d8704832", expand=False, url="https://files.pythonhosted.org/packages/d1/6e/3d6bc13f6987c609092e9c2f87aee44e726492d463180d680db3dc5220b8/nanobind-0.0.6-py3-none-any.whl")
    version("0.0.7", sha256="db30105ca6a8eddd7db9da3b1fd14d4e07bad3b6a60322bbfb0836eccbc0250b", expand=False, url="https://files.pythonhosted.org/packages/c6/3a/1b27b59c4bbb813c9a7ed23b5c273b6e467ad299eae22ca4bf6b94a196c2/nanobind-0.0.7-py3-none-any.whl")
    version("0.0.8", sha256="5d5eba535baf49302a0c5de8296033d7b69a883f3fc2a8e3022b27e0025f3e3d", expand=False, url="https://files.pythonhosted.org/packages/ee/d1/86d5e551cd0df78f5df813898dd73eee1bcdc40f6851b463ad888cfe6e34/nanobind-0.0.8-py3-none-any.whl")
    version("0.0.9", sha256="e7117596c8bdc72b907be1a8d16e5f37e0c4f5fadbceba9e2abc4e786f4f8671", expand=False, url="https://files.pythonhosted.org/packages/04/bd/8c3fa22737db8d34ce88971a52cb4f645cf7b07701237795f1264629b090/nanobind-0.0.9-py3-none-any.whl")
    version("0.1.0", sha256="25b8dc37f1902041d282befd33a10e7bf3b0a4ced8cc58a700532379a61b9b76", expand=False, url="https://files.pythonhosted.org/packages/6c/3f/577521c31ce51eb4266d1c3e66eceaa902f9526e4a8259aa3012ac706b95/nanobind-0.1.0-py3-none-any.whl")
    version("0.2.0", sha256="b38b4d44e7efd82468602696af70844e596787a7987f39ef08b8a2f55b779dcc", expand=False, url="https://files.pythonhosted.org/packages/e4/4a/d287d8b226bb631120c69351cc58e3cf4cdd3ea778aafb579dafc9ea163e/nanobind-0.2.0-py3-none-any.whl")
    version("0.3.0", sha256="636829b3f6bb025c3ed0e684e53a33871c7d5aa8a1b8003982b8a320d584c804", expand=False, url="https://files.pythonhosted.org/packages/85/21/e3264d20df19e6cead01ed5851ca5c5a53e4b9ea3f5c9c5b8bdcb321d4a2/nanobind-0.3.0-py3-none-any.whl")
    version("0.3.1", sha256="daf2f56fa1cb7869bc4aaf6194e87a054fc1a8f78de71a4ab8c157a55c5dd77f", expand=False, url="https://files.pythonhosted.org/packages/63/de/a052e81d279fa8bae3c2cf34cc395d28ff31b2ad87d7fb0ea4d26be9a2fa/nanobind-0.3.1-py3-none-any.whl")
    version("1.0.0", sha256="6ef06c7c2176c185c5834bab327105ff71c07f821d1ca7c389d350f438e82ce2", expand=False, url="https://files.pythonhosted.org/packages/08/f0/e5cb4561e084c436ec1125c0b2869cc4d377ce2402ec0492b99834e2ef3a/nanobind-1.0.0-py3-none-any.whl")
    version("1.1.0", sha256="55f82ca45a497fe33e7c9d5847fc369cb89f4ac790b6b9b9fdb5ca0a3357189a", expand=False, url="https://files.pythonhosted.org/packages/2d/3f/44bbc9f49d5438b353c2196209fa38b63173d852495f03640c3add151ae7/nanobind-1.1.0-py3-none-any.whl")
    version("1.1.1", sha256="4e2e30234f933f5888c630aa229b1d339a84e4d0dfa62499335e15db3769ef6f", expand=False, url="https://files.pythonhosted.org/packages/72/c8/aa058929be774f382c46e6bf83733395712d001af50afa58dfaae17c1624/nanobind-1.1.1-py3-none-any.whl")
    version("1.2.0", sha256="949332ba8653a7dedf1ebb24855a4479116e7774478240213a00493db3c49e9d", expand=False, url="https://files.pythonhosted.org/packages/a8/39/16ef46072bbfe55fcb5f7f0884befc06ffeae304c9ad1a2515029471c21b/nanobind-1.2.0-py3-none-any.whl")
    version("1.3.0", sha256="a7c642c68b638c662b50de1b445b28690c3100542d77ad4ce096fb8d9a66c2b5", expand=False, url="https://files.pythonhosted.org/packages/93/6e/43f732d8f62be9ffc4a948e872c99932af56e7462947e1484a86393e8fe2/nanobind-1.3.0-py3-none-any.whl")
    version("1.3.1", sha256="70aa6f540345b98bd2dbcf1061d902db658cd2eed60ee66e2b8305766bb3caa1", expand=False, url="https://files.pythonhosted.org/packages/e6/04/ff8c4cb80df32fa3ceda3c379021290789fc467816ec58f6126cb175e344/nanobind-1.3.1-py3-none-any.whl")
    version("1.3.2", sha256="bf0b0a0954e9faa682fb8ddd57591de86e4bb04e88d0293c4fddc28fd4d2b872", expand=False, url="https://files.pythonhosted.org/packages/46/67/f3e50c54f061f93741e5b289264a6efdac2a0ece7cf15bf0aac55bfeff76/nanobind-1.3.2-py3-none-any.whl")
    version("1.4.0", sha256="0eeded0d18368e2b575714dc620e85631ffe03eb719f8d629101abb2c09668d8", expand=False, url="https://files.pythonhosted.org/packages/67/ce/1b20a4c92f607eb7229775c0babb409484e5d62fcecc083f8d7d0a8b5270/nanobind-1.4.0-py3-none-any.whl")
    version("1.5.0", sha256="0e23436bdc7246c332eb4bd477b89b53482490457a12d7b084a9b410f122770b", expand=False, url="https://files.pythonhosted.org/packages/ed/ea/5e806594f91cdbc00897acd990c2f5778f37bef0deb94ae03ac66cba4a1c/nanobind-1.5.0-py3-none-any.whl")
    version("1.5.1", sha256="e4408ca6bcd424cb4555c6217cf7624d334862a6d497c549b01b9bc509e25b21", expand=False, url="https://files.pythonhosted.org/packages/cd/90/300cac4677ffdd95c5fac9cd1a64348370ce7f5f30e6c1042642ad907b1f/nanobind-1.5.1-py3-none-any.whl")
    version("1.5.2", sha256="34515bf2c0675d6d1c7be17ae8c7a1361439cb0a98dcde15899f23a63ef1b55f", expand=False, url="https://files.pythonhosted.org/packages/96/8a/fbabb2a18dbf16343ca34c6d6dcc019365f9683eb79d5cfcffe18a07689a/nanobind-1.5.2-py3-none-any.whl")
    version("1.6.0", sha256="2001abde1d86e6732ffe88ad299f9881c417615d537a605b0e837b347ff4d2e0", expand=False, url="https://files.pythonhosted.org/packages/a1/77/fd474905a3d39c57d4d64349a80362a4ecdd90d927eb38e2884e2bd40d7b/nanobind-1.6.0-py3-none-any.whl")
    version("1.6.1", sha256="f3aa048341c3cf2916b3da2c20816871522eb513efacf8a9504bfcf4977eee93", expand=False, url="https://files.pythonhosted.org/packages/42/83/20cedf91fca25b98e1d3c901fa80f13c674eecb1bf3754dea0252155ae36/nanobind-1.6.1-py3-none-any.whl")
    version("1.6.2", sha256="27b62eae0134cd60563a4026e5f347d88fcae6d6357b11683b470eb4c51efe9f", expand=False, url="https://files.pythonhosted.org/packages/dc/79/343cdc299ce8d4569f906284492c31c62482d6fade5b53c9ecd818de5dc3/nanobind-1.6.2-py3-none-any.whl")
    version("1.7.0", sha256="a368b8121d3c1ec384a2dab0cb2b556924ceafc84ed80b0d1e211e3997576dae", expand=False, url="https://files.pythonhosted.org/packages/8c/cd/0520686bf2e367e6ef6fb11992161b5d8807a488fa9985572400816a8102/nanobind-1.7.0-py3-none-any.whl")
    version("1.8.0", sha256="c9b069f408660124b12565ca026834d146154a3965efcd2bcf749eefb99b4873", expand=False, url="https://files.pythonhosted.org/packages/3f/35/73cb6560af76dc75257635875d033111f1ac324e1cfd4b953d442e874aac/nanobind-1.8.0-py3-none-any.whl")
    version("1.9.2", sha256="137ba9e75cc6b2e5d92c2acb9810beaa079b9c8e5d68c581b4f90d626d79358c", expand=False, url="https://files.pythonhosted.org/packages/62/e6/84bdfbf05913ec5b4a426e5ba614d4df669c66929376dde96d6d55da3199/nanobind-1.9.2-py3-none-any.whl")
    version("2.0.0", sha256="9e4f4383ad83a72ce46ba5e9395dc67fadb8d53e5230aecdfc90ffdcd08d1a70", expand=False, url="https://files.pythonhosted.org/packages/de/54/e9f3ff609d525c2bfe7a1516964f1f4543806f1bb34b8e27d30f2aa9f5ce/nanobind-2.0.0-py3-none-any.whl")
    version("2.1.0", sha256="a613a2ce750fee63f03dc8a36593be2bdc2929cb4cea56b38fafeb74b85c3a5f", expand=False, url="https://files.pythonhosted.org/packages/31/48/dea3d75657366b5a75b9d57a4e4fa7b224d98e8385f72fc7762d504533df/nanobind-2.1.0-py3-none-any.whl")
    version("2.2.0", sha256="138685ec9c5de4f57dd02d715b89ffcbcabae39c4e36b8b2c40eea2f1aa2f0d7", expand=False, url="https://files.pythonhosted.org/packages/52/af/7032b05a35284e741666acbf3eac3a14b5e81cd92264ac775426884ed460/nanobind-2.2.0-py3-none-any.whl")
    version("2.4.0", sha256="8cf27b04fbadeb9deb4a73f02bd838bf9f7e3e5a8ce44c50c93142b5728da58a", expand=False, url="https://files.pythonhosted.org/packages/7a/07/abff41fcade3613349eac71dacb166352babef515efd960a751e3175c262/nanobind-2.4.0-py3-none-any.whl")
    version("2.5.0", sha256="e1e5c816e5d10f0b252d82ba7f769f0f6679f5e043cf406aec3d9e184bf2a60d", expand=False, url="https://files.pythonhosted.org/packages/8e/9e/dadc3831f40e22c1b3925f07894646ada7906ef5b48db5c5eb2b03ca9faa/nanobind-2.5.0-py3-none-any.whl")
    version("2.6.1", sha256="678be25b6ffdb7e3776548c2c9f29072e7eb41219b72c51f8e14ac0fe5c8ae0b", expand=False, url="https://files.pythonhosted.org/packages/26/f9/0b11e9b99a35dbf91972845af6012c562f3f1845a33e5b4ea631568d2740/nanobind-2.6.1-py3-none-any.whl")
    version("2.7.0", sha256="73b12d0e751d140d6c1bf4b215e18818a8debfdb374f08dc3776ad208d808e74", expand=False, url="https://files.pythonhosted.org/packages/96/14/989883082b395146120d34ca7e484a2b24cb73b0e428576a3a4249bd4082/nanobind-2.7.0-py3-none-any.whl")
    version("2.8.0", sha256="80fd403cfe4c8553b237ba5fbb62971921e2c5d1e6eb4a2fd457c67f987ab56f", expand=False, url="https://files.pythonhosted.org/packages/fc/3f/d81fa4c0d1450c6f58f5b5708082617949c12c5e98c1fae0d94a9e3a9b8f/nanobind-2.8.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
