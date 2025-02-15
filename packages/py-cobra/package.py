# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCobra(PythonPackage):
    """COBRApy is a package for constraint-based modeling of metabolic networks."""

    homepage = "https://opencobra.github.io/cobrapy"
    pypi = "cobra/cobra-0.9.1-cp36-cp36m-manylinux1_x86_64.whl"

    version(
        "0.10.0",
        sha256="c868ba17257306e9980188180904f6c1c0f8d5e1712a2844eff6961f63a4e435",
        expand=False,
        url="https://files.pythonhosted.org/packages/eb/0d/d39b9b311bed687c6928beb66ed6d4d8642312c2c5f9be2b761a8325f119/cobra-0.10.0-py2.py3-none-any.whl",
    )
    version(
        "0.10.0a1",
        sha256="a14ac21374605cf427ae48e27943a5f374a2e36fa20d02b38ad45c13888902a8",
        expand=False,
        url="https://files.pythonhosted.org/packages/ab/e2/36ace506f74cfc67eef011e030da5c423a47749bea4e1f2af3a20b571380/cobra-0.10.0a1-py2.py3-none-any.whl",
    )
    version(
        "0.10.1",
        sha256="17584a431059e6f885fceb3391f5fe798f19f049fcbc6dde2548ba30b99fac53",
        expand=False,
        url="https://files.pythonhosted.org/packages/e9/8e/c123af50b4351c6deff443be542ab7d8c5d41c3eaf8f6422015569d34af5/cobra-0.10.1-py2.py3-none-any.whl",
    )
    version(
        "0.11.0",
        sha256="21940a067dcf72eabadeece3e05090f7ac191cd80e25e1a84b57237e50f233c8",
        expand=False,
        url="https://files.pythonhosted.org/packages/cc/3a/2cc2bd09ae2153fbfd9a2e1872fee0fdc66c559158f9a9771cc0b117ef70/cobra-0.11.0-py2.py3-none-any.whl",
    )
    version(
        "0.11.1",
        sha256="82d7de3f19d9f79a72bd924f0b7a2abb7830af04b5a3b506cf33ce98c054405e",
        expand=False,
        url="https://files.pythonhosted.org/packages/8c/92/bdf21aaaa4d59a7cd8fcef0dabd3590b5729aefeac74ca5bbef0745f0cc4/cobra-0.11.1-py2.py3-none-any.whl",
    )
    version(
        "0.11.2",
        sha256="9ab45bf03a66c3f24cc65668538807d2a7b082b9e70e281df234d24cdd32e60e",
        expand=False,
        url="https://files.pythonhosted.org/packages/43/8f/b0d2a366d88c7d7413111dc525f4611164c96e300f2d882f5a15495febba/cobra-0.11.2-py2.py3-none-any.whl",
    )
    version(
        "0.11.3",
        sha256="28a6e38e77b83f3895416c0d15edf198c37ede1775d74edaeb07d88bb423049e",
        expand=False,
        url="https://files.pythonhosted.org/packages/d3/00/0bbfeeee739b0809d0f475726799b206b9590f6191e34ef1e4e2caa34e8e/cobra-0.11.3-py2.py3-none-any.whl",
    )
    version(
        "0.12.0",
        sha256="10aaac887d2b3310d9fc0f08171e303d90d4dcb6c2ca0eebb22329d001244725",
        expand=False,
        url="https://files.pythonhosted.org/packages/45/e4/aa2e72a8edcdf154b4feb06d982396307c8fe2608beb7963b415f8d56227/cobra-0.12.0-py2.py3-none-any.whl",
    )
    version(
        "0.12.1",
        sha256="341af6c7f441ef83908d8c569e49e118e29061a5c10df7a4c16bbfaf401db7cc",
        expand=False,
        url="https://files.pythonhosted.org/packages/37/36/fa419845123455edab8743405f1a00704d0b8ba362d85af1a4f6fb2ac6ae/cobra-0.12.1-py2.py3-none-any.whl",
    )
    version(
        "0.13.0",
        sha256="ef0f8507ec2bf255e883e073507cb1b61af43af7b20d741af93d71547afaf0a9",
        expand=False,
        url="https://files.pythonhosted.org/packages/05/5e/244535893f1fb3a61ee1da2c85f8f9c242f22e4ccc5c8881bfb20d51f1b7/cobra-0.13.0-py2.py3-none-any.whl",
    )
    version(
        "0.13.1",
        sha256="a71a4cbabfe97ab39a9917717665bb6b47dd67aae62c5db4829c3ac0ba5d3965",
        expand=False,
        url="https://files.pythonhosted.org/packages/a1/3d/30610365b78768abd880838b9c110ecc0131deaaf2ebabbd6bad7b1a4535/cobra-0.13.1-py2.py3-none-any.whl",
    )
    version(
        "0.13.2",
        sha256="a643ee2838f30875f0df4e89b411f4059e8e7db29e2221069fbcfa9a0692262d",
        expand=False,
        url="https://files.pythonhosted.org/packages/56/9b/f84a050347a04e379dc330dd740de5e7c9c304b04738189fdbd7f28463b4/cobra-0.13.2-py2.py3-none-any.whl",
    )
    version(
        "0.13.3",
        sha256="75ec0718e080797a74f109e58b53ad238edbf2dbf4d29ee1a37c95234423842b",
        expand=False,
        url="https://files.pythonhosted.org/packages/bc/70/5f6a5f9914b8475cc68e0318d7c5d1f54eebc1afc5229ee2031affb1be89/cobra-0.13.3-py2.py3-none-any.whl",
    )
    version(
        "0.13.4",
        sha256="90f1d498543f615b53357269a2ae5fd6aa27daaf3de8cdcc6fbdac4ec48ad58c",
        expand=False,
        url="https://files.pythonhosted.org/packages/e9/f7/7af37414edaa279e59fb58f4cffc30869035b87f2b2d6ad83a19bd7a03fd/cobra-0.13.4-py2.py3-none-any.whl",
    )
    version(
        "0.14.0",
        sha256="941f0562d7b8c2570c64dc0d676e434d67e69e082c765f9d0a58f7415509d690",
        expand=False,
        url="https://files.pythonhosted.org/packages/38/b4/dc4ae4799375a43dc8e6b1174bcd378b22eb87b21c928f7911444f0731ee/cobra-0.14.0-py2.py3-none-any.whl",
    )
    version(
        "0.14.1",
        sha256="e20f126e0ab8b37575a282a5bc5a5028a0be4b95b652dae00ff9f4dbc8b0c3fb",
        expand=False,
        url="https://files.pythonhosted.org/packages/0c/bd/346dc44c9e402266f91324c894bf6ed32dbce3f818f7bca5ae56e646af20/cobra-0.14.1-py2.py3-none-any.whl",
    )
    version(
        "0.14.2",
        sha256="ac3d815831eb4316c72a60b3882088319e658e8be4ff341aa342d0a96c093258",
        expand=False,
        url="https://files.pythonhosted.org/packages/d3/94/12ae5e185ad8e6bb71cd240988df3cb1378261d5bedcca3f28229cb0eb59/cobra-0.14.2-py2.py3-none-any.whl",
    )
    version(
        "0.15.0",
        sha256="b5bab9fb0fe1eca47ed368d7d6426cee9f9b559d867ba27bb468bf7ce10b5b17",
        expand=False,
        url="https://files.pythonhosted.org/packages/f9/d2/a2b3fdcd964dcc8a7c98b7e9953a9f899856c2c52bd6c9bde170f407b617/cobra-0.15.0-py2.py3-none-any.whl",
    )
    version(
        "0.15.1",
        sha256="c6d35f4d8064d97f68af74adab70f315251c557a528f0d7ca42a0b9e655168dc",
        expand=False,
        url="https://files.pythonhosted.org/packages/08/ce/660cf551955a2fb72f121efee004e4d21a947e99aab908e27d031730d0f4/cobra-0.15.1-py2.py3-none-any.whl",
    )
    version(
        "0.15.1a0",
        sha256="72c36561157f50e4316180cc5170768c4ff591c11eb5495fc07d619941bb4201",
        expand=False,
        url="https://files.pythonhosted.org/packages/03/e4/8f2f9e51ca7002df65874cfe86cce8dd9949a5f5cc485c12bcc785f315f1/cobra-0.15.1a0-py2.py3-none-any.whl",
    )
    version(
        "0.15.2",
        sha256="c2c6409b6c327c6556153ca96c58052857f23e67f2ff635828a771552b0e76b3",
        expand=False,
        url="https://files.pythonhosted.org/packages/67/3c/2eb493f44969a6aed328da758b592b2de95ad1bb7e325feda78885cf366b/cobra-0.15.2-py2.py3-none-any.whl",
    )
    version(
        "0.15.3",
        sha256="b9a3fa4f12f018c727f5ff852da67d43351ee9b056873ede237485e551f9e5c7",
        expand=False,
        url="https://files.pythonhosted.org/packages/37/fe/ef6909498b2ba870d331251840ffc7d8f1d6d69a05bb8305c5beef78e39e/cobra-0.15.3-py2.py3-none-any.whl",
    )
    version(
        "0.15.4",
        sha256="cb62dc939e7a738ce6352175694bebf0dfff14985d949310d07e138bc6d4e3d2",
        expand=False,
        url="https://files.pythonhosted.org/packages/76/64/961ce89b50edbfe44a198e5867bfb788d135cc6b92a16dcdaadba6716815/cobra-0.15.4-py2.py3-none-any.whl",
    )
    version(
        "0.16.0",
        sha256="fb3c6816e7b7c6524f96b185ca6735b3c57326ee38cc644eb358fadaf01f9c67",
        expand=False,
        url="https://files.pythonhosted.org/packages/f1/2b/980374a9ca930f95499df0787e8efb0a4d19784a911b1df4d2dfc4c4517c/cobra-0.16.0-py2.py3-none-any.whl",
    )
    version(
        "0.17.0",
        sha256="1c2eef90891f594e684e54f4262588fa9dce095f79d04366cef631dd60833ccf",
        expand=False,
        url="https://files.pythonhosted.org/packages/7b/de/eb3c5bea88e39de0a6a7a28da40f64d6cf1e31c38b96aea69102e117160c/cobra-0.17.0-py2.py3-none-any.whl",
    )
    version(
        "0.17.1",
        sha256="31be1a1c5ebe8e794f71068e63a5ec052c667a9bab02837ae5e8dea4a934343f",
        expand=False,
        url="https://files.pythonhosted.org/packages/c7/49/24ae8af404bc3d1135a6a50ee70478806205bee14a4b5addc554612276f4/cobra-0.17.1-py2.py3-none-any.whl",
    )
    version(
        "0.18.1",
        sha256="027807437de57f4f63fc4ceadf13c569c8baffd5acf1e4c1ecc1e07260edd966",
        expand=False,
        url="https://files.pythonhosted.org/packages/c5/64/b5e27f52f959644a9e4acd04f4b3686f4ec6cabebb311e7ac73dd49abae0/cobra-0.18.1-py2.py3-none-any.whl",
    )
    version(
        "0.19.0",
        sha256="385c5363799e644b452616c82e4b1659992004b6564a626d6b886dab9c2c532a",
        expand=False,
        url="https://files.pythonhosted.org/packages/88/78/7cc3c0b614f676911b6141b6c48e29b9a3f15e335061d0684ed686662b4c/cobra-0.19.0-py2.py3-none-any.whl",
    )
    version("0.2.0", sha256="3ee99102b60ffb91cd85cb2e198427b0106f69dd498765e18195791bac6e9f60")
    version("0.2.1", sha256="3cdbbd823466dff6e7ac31d9391c3d7fa36ef3f57338b269e23d4b9bf98ed4fd")
    version(
        "0.20.0",
        sha256="d49cfb582fc5e2c9917617c0b0b8732de2e1df6f282b3ecdf23755176a339c58",
        expand=False,
        url="https://files.pythonhosted.org/packages/dd/11/f3559107796b272051c4418d2f54df449fb4fe2a65a9350a61912785d854/cobra-0.20.0-py2.py3-none-any.whl",
    )
    version(
        "0.21.0",
        sha256="dd8cfa1f6df99e91e99820d213d496014730025abce142246dddf61a3b080bf8",
        expand=False,
        url="https://files.pythonhosted.org/packages/9c/c0/bea19dbbe6e4907a591272100717f491b82ff8a485b4ff1528182532bbcf/cobra-0.21.0-py2.py3-none-any.whl",
    )
    version(
        "0.22.0",
        sha256="9ef683a9debbd0d670cd237ae5d101b225b0289f91ddf7a5a65673fa9908459f",
        expand=False,
        url="https://files.pythonhosted.org/packages/c5/04/f785d34e11b42b21c101130d60324c90f58a612f49a6f95e1747f0f05ca1/cobra-0.22.0-py2.py3-none-any.whl",
    )
    version(
        "0.22.1",
        sha256="f9c3fea3c1d60eb8b317a6ba047d3fb29d53b85235f22d3d38660be8a4a51bf1",
        expand=False,
        url="https://files.pythonhosted.org/packages/ef/d7/bf3ce6b385a1a31168fc5c6e17d93bcbc787a7140207d7f50a31e22daaf4/cobra-0.22.1-py2.py3-none-any.whl",
    )
    version(
        "0.23.0",
        sha256="65acd7e55cb7abaca6c4f7105c37ecffd2e39ea5edf0c2b80641a339f1fad3a5",
        expand=False,
        url="https://files.pythonhosted.org/packages/8f/31/1e45611016e3b4064c567225345ef262fc73c0bf7edb92553565b9bb488a/cobra-0.23.0-py2.py3-none-any.whl",
    )
    version(
        "0.24.0",
        sha256="6c8dbc312f82bdbd47ecd16a59f04b22ed3feada6d92d08a1a99aa8d070e8d9f",
        expand=False,
        url="https://files.pythonhosted.org/packages/29/1c/63549e9e73ad4faa2d80700da1c8e4ca13836adc95201efa476a7387560a/cobra-0.24.0-py2.py3-none-any.whl",
    )
    version(
        "0.25.0",
        sha256="6ab6b6b9cec435e2ac5a4746d348dacf338735488f8be2e699f39720fe99eb22",
        expand=False,
        url="https://files.pythonhosted.org/packages/4a/7f/7ddd092dcc24f8381409e63a357aa8fba13f9743cb25ef1be2ade1569e39/cobra-0.25.0-py2.py3-none-any.whl",
    )
    version(
        "0.26.0",
        sha256="305cbbc24f0269aba614bb1e82e2ca80a153dcd3ed4380f6d58368940d0ac7e3",
        expand=False,
        url="https://files.pythonhosted.org/packages/79/45/e4a30ef8c466532e9443a3a245f9f8c776500ffde33baf659e2195871bed/cobra-0.26.0-py2.py3-none-any.whl",
    )
    version(
        "0.26.2",
        sha256="044d74ccc3f3c481e5d4aedaac54c129ed1d8b0b528ce55f829d843a1d43d405",
        expand=False,
        url="https://files.pythonhosted.org/packages/dd/2b/2c2f0973dead88b6f35886f67e216c0bbbce4cbe2069cfc282d2ce79d1b7/cobra-0.26.2-py2.py3-none-any.whl",
    )
    version(
        "0.26.3",
        sha256="efd75ba1b2d12bb64d88ec67bd6037d76eaebb2af349f314090dbfedc424201a",
        expand=False,
        url="https://files.pythonhosted.org/packages/e1/08/2f01e494576b89be0a0f357da4a2a3d4f8213bc78754e88702fa02b914c5/cobra-0.26.3-py2.py3-none-any.whl",
    )
    version(
        "0.27.0",
        sha256="7787df0df9979e5d63398da2c2462b146606438f99b5540edf8c284d159ea606",
        expand=False,
        url="https://files.pythonhosted.org/packages/9d/03/99141fc78157a6bb306d395d206cf7f1494856f215d91e4dc3cbaf13b261/cobra-0.27.0-py2.py3-none-any.whl",
    )
    version(
        "0.28.0",
        sha256="ebacf19a76b613855b27f02924eea9c66c76d7ef975802a23a226ab085fa1deb",
        expand=False,
        url="https://files.pythonhosted.org/packages/85/41/9ac0e87ea7c47f50e8e120064300d7fb6f9dd6080aecdd1ffd56181fffc4/cobra-0.28.0-py2.py3-none-any.whl",
    )
    version(
        "0.29.0",
        sha256="9a9bc4ed1a027c22c5fd4fed111cce7606cda3cdfc44587483c35714ba4dd9f0",
        expand=False,
        url="https://files.pythonhosted.org/packages/8a/82/758f8a4be7d951c21533bc20d61ad4bfcaef58084f45c045ef069c9fb96c/cobra-0.29.0-py2.py3-none-any.whl",
    )
    version(
        "0.29.1",
        sha256="734df889e751171c12ee9c5ec6f2567f47f9997e183822d4290776aa650c9593",
        expand=False,
        url="https://files.pythonhosted.org/packages/12/5c/f586d381e8307c2c46d4b382c23f50f3ee023e3d811cb0e7ae30b364088a/cobra-0.29.1-py2.py3-none-any.whl",
    )
    version("0.3.0", sha256="a988ae8d3d89253d13c25baf4c1820a407c0a3b5cc54058f7d554ab77cdcf2f5")
    version("0.3.0b1", sha256="62f4b77a41f4ebec9f40509a9cea362ca73e9055c72437f697a3294eb953b63c")
    version("0.3.0b2", sha256="a864be49312f9e548b2aaf6b354988bf0da5af6f75b97e9bc8ab8c62962fd7d0")
    version("0.3.0b3", sha256="1cf986db016e205ac95ffa34e722a14d90babb39895ddd6017053a47dbaf4b8b")
    version("0.3.0b4", sha256="837e196ffe96142b1807529c44c9e5a2445b158d56305123593b094c15efd720")
    version("0.3.1", sha256="82e9f3400f16cb37d384881609505b76ebb82891f19f3729e7c199c47e926e4f")
    version("0.3.2", sha256="28a13a377a752da7b2c3386078f333123724c171761617f673770149c0aefa4a")
    version("0.4.0", sha256="104e1f73f78d463849161143e8f2b98fcd7cb5ce8ee2c5b0c704ce3153036e30")
    version("0.4.0a1", sha256="1a30629e06c067e638f5f7c284822b305464f34727a903315d98d70c253de378")
    version("0.4.0a2", sha256="4bd81d92493a45ba6a4eb86e80785c72bf12fe6307aee52db2c4e364661100b2")
    version("0.4.0a3", sha256="298dbf592d1a5e4e20d7f6d61b9ed7c63055cfda5c167f3da45dd904264d4e36")
    version("0.4.0a4", sha256="936a59402ba7401b7d5a663a2c027cce88c46eb634462a1841067f7baea9e7e4")
    version("0.4.0b1", sha256="920257b6d14da070b58a18e28379d1ac8183a62cefe709de38a003248a640c14")
    version("0.4.0b2", sha256="42f24388de1f443c16c7906f4d9ee3aaaa80d34eb38c82e467e5ebe9bf9ac28d")
    version("0.4.0b3", sha256="81909c5fe6cc0367e68ff0c4b4a76ed5ec71ba2b46495fdda33b0f0f056dfaad")
    version("0.4.0b4", sha256="0a3b13c955422c9ff63287cfad66897185c748a49af889f62b12655f906a8e24")
    version("0.4.0b6", sha256="7a8b0e3e3d61a93e162a14b4526342ada6318123d4f0d948e546ac48b0a1720e")
    version("0.4.0b7", sha256="065c4170a09619824ec4c82d2988a9bd39560bb42db2f87d10908a1da1a9306e")
    version(
        "0.4.1",
        sha256="eebec3b8f995894c2ff2465b370aeb8cd567f21b7fd10b68a923d40e16647289",
        expand=False,
        url="https://files.pythonhosted.org/packages/42/df/71886f8f7d3fed1526a0b8f0650d9e505c18605b9a50333c5b4734febac9/cobra-0.4.1-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.4.2b1",
        sha256="9835bea954f107cc4d689eeaf5a0b8bafd495346ffc668b456a9ae1ee1a3f710",
        expand=False,
        url="https://files.pythonhosted.org/packages/81/8d/250a083ff300f4ee2ba5006311e0787cbd1d3e3de6c39b5108ac7f923470/cobra-0.4.2b1-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version("0.4.2b2", sha256="ccdf786de0d583e401a54fba0c8a9ba2e69fbfbb98a810a381e0045bc13dc839")
    version(
        "0.5.0b2",
        sha256="975125e2413cf9903548683b43b068f6e4b64248364371c9a64c1752cb6adcd3",
        expand=False,
        url="https://files.pythonhosted.org/packages/25/a5/de1c2cb64080e8d00c29c914f63bace1cbc8ad5757da5c9ea1f2e9396f46/cobra-0.5.0b2-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.10",
        sha256="0270e61dc8af4742115e055d356c4b00fae42efffd981b0080f0afd4e3ca584d",
        expand=False,
        url="https://files.pythonhosted.org/packages/13/93/a2fd81393b453e459b049ed3c7ba093998d8353a846f56b235b1b6edc6a7/cobra-0.5.10-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.11",
        sha256="94881263f6cbe4305ae6a124e9509272fac665ed111254d605a0c7655248d1a8",
        expand=False,
        url="https://files.pythonhosted.org/packages/cc/a2/7e73c9f9e8b207710e1a579269ee9b00d21e3d5104c56f777114d318a817/cobra-0.5.11-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.1b1",
        sha256="699b813d5fe911e8c2bc62f19b5d0a91634a09f5c2cf9fb60bd4b63231c0ad30",
        expand=False,
        url="https://files.pythonhosted.org/packages/9b/75/77c305746f245243079bbe69066b974a0741792bfd5c3f5873fdc47c54a2/cobra-0.5.1b1-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version("0.5.1b1.post14", sha256="ab8ce0bfe590b627326a578e80842b1f63f65e5524f6500b1e8866c0248e0ed7")
    version(
        "0.5.1b2",
        sha256="95c107d0977e67fdc6c93ff5942fe3f3ee7b308204603ee9da60be6617f4163e",
        expand=False,
        url="https://files.pythonhosted.org/packages/69/71/3817fe7cefbd88f622def45747cfd72b88da7f78340d1cd246400b8ee0ce/cobra-0.5.1b2-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.1b3",
        sha256="a8f1826a1727c1051f9a4c880553b512642232d3b840e133962ab131b5b25847",
        expand=False,
        url="https://files.pythonhosted.org/packages/c2/1a/8354c6a818afe24999476bdfde4300cc78dc24501cc86fa785a238dffd4d/cobra-0.5.1b3-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.2",
        sha256="7317e8ff5763c786dde11b03894842685a99626240f8be6aca869fb3e19d65e0",
        expand=False,
        url="https://files.pythonhosted.org/packages/43/7b/1fe62e2746eae70e14888fd60f79247a5a680aabb9eed703194ea59072d1/cobra-0.5.2-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.2b3",
        sha256="2e020843515f0479b796b09f5c861eac7f9e5643c05ea93e0f0aad22acbbf8e4",
        expand=False,
        url="https://files.pythonhosted.org/packages/27/9a/8382483b2cb1a9445e3d666bf9a7dbba84ebadc39b93b348c55a46fd3b8e/cobra-0.5.2b3-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.3.post3",
        sha256="1c8f0c8a1400882af2ce0ac3b3d3e055d0ed03a0b48db11c5fafe94a7814e958",
        expand=False,
        url="https://files.pythonhosted.org/packages/36/26/6d0b35a7cde624011af8f3fd3827417e426574b9a28f135fcea9616b5655/cobra-0.5.3.post3-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.4",
        sha256="6da80e378ee2838cd56e5cfadcde674ac2e4a0c220ccae43338be2a319573410",
        expand=False,
        url="https://files.pythonhosted.org/packages/99/b6/936a58fec97d1c6f205dbb60598dd4d903a53312804e1a5f7fe40ad9d7f6/cobra-0.5.4-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.6",
        sha256="72a803c5a0b2ab66c848dd80756ef8fbae6e78560acc6161ea5c677cc9c745d9",
        expand=False,
        url="https://files.pythonhosted.org/packages/0d/4c/f7802c7728558600146cf31168162dc09465049135d0cd6f32cc114f4aca/cobra-0.5.6-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.6b2",
        sha256="1f8381dd4015559353a4bd345445cda5e93c8a7acb7138721f2bfc3c877aba79",
        expand=False,
        url="https://files.pythonhosted.org/packages/c2/73/f94b3fd993e56c5c259f6fad41959735ac408b08842975202faf898e5b03/cobra-0.5.6b2-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.7",
        sha256="b41aa970ba911240540f8db8e80afc63c296bb4ccd2846d97e4aebfa22831432",
        expand=False,
        url="https://files.pythonhosted.org/packages/d1/a5/12969088ce89aa3879991f45ed1179933af219e634f6c1b1d0b6307a4174/cobra-0.5.7-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.8",
        sha256="65c3177510d1186ff980e506525fb1b3d4ea1a06774152a49f170c9d8ac036b8",
        expand=False,
        url="https://files.pythonhosted.org/packages/a7/9d/10313b178d53029ea5f146157f3e2f6727ea14b76486a419fc38d34fe8a4/cobra-0.5.8-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.9",
        sha256="926e166379650299a1325c7284adf36fce3c0dda3d1141cab1df20505d72a7c6",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/e0/86a1aa32f42edf377860bdcd2ac5e5f8b085d15cf8515c819d0e23e96781/cobra-0.5.9-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "0.5.9b1",
        sha256="379a8a2ed6a4f4d6c5d15d23d693f1021bd1a9868097867191d5e77fefc64881",
        expand=False,
        url="https://files.pythonhosted.org/packages/3d/af/cccd10528e4f442b72796975d2dec3b2bd0965cae37b6d3e7d5bd0262222/cobra-0.5.9b1-cp34-cp34m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0",
        sha256="10018ba1452dcc478d54fdc1d65b3573810372903a1b862dd27eed55a10780a0",
        expand=False,
        url="https://files.pythonhosted.org/packages/66/76/9f8783b84fa05587a1d1bcdd63b5250594ae31a0e920b59786d61fb9ef58/cobra-0.6.0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0a1",
        sha256="345e9f9f15b2a154fb651c2029dd810fb9360c1c34630203e11e41a9ec07d7dc",
        expand=False,
        url="https://files.pythonhosted.org/packages/89/ca/681b9de3d5810ca6e737525d3c94cdd513dec986be5e6f9d7547cdeb67d0/cobra-0.6.0a1-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0a2",
        sha256="e1b1e382b5de5835d565b7e213520db2864a4d3d70da4f9da0793fca63498a83",
        expand=False,
        url="https://files.pythonhosted.org/packages/49/20/49c37c1321462a626d12307bf2405b4986be5726e46558f602f77501b312/cobra-0.6.0a2-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0a4",
        sha256="ecce8d08cece9ad6f08ce71fd022a92ceff653eafd674acbe836b6828cd620b7",
        expand=False,
        url="https://files.pythonhosted.org/packages/71/c9/179961ba48af0b9026a9c98fbc5d8311679cc813d769f0b3615bb5a8d0af/cobra-0.6.0a4-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0a5",
        sha256="18bfaf79efce357ab448580aa8e5aa1afecfbee2f03952c39c1e17103f33811c",
        expand=False,
        url="https://files.pythonhosted.org/packages/5f/28/dad4df925a955653c41e7b17cf84f2ac99e6267d2343930ce55220a4d640/cobra-0.6.0a5-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0a6",
        sha256="99039edceb078a4a9d59d7f73dafeec2b87c971f438ec15cbd40afbadab54384",
        expand=False,
        url="https://files.pythonhosted.org/packages/9f/7d/bed022370a1b69cfe9e43499d499c53f15ea3594e27a05c134678bc6f475/cobra-0.6.0a6-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.0a7",
        sha256="7c119868c09f8a2ad2e799e47fae093c2c1d6abc291bc0c027717f0ba47be8c5",
        expand=False,
        url="https://files.pythonhosted.org/packages/27/5e/688db843ba8687d353810dccf9723541f11de77f3756382b494578ae8089/cobra-0.6.0a7-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.1",
        sha256="53eaaf8bb76dde77490b19a3e08d73e31902f0af55100b3f82c8a457181e5b50",
        expand=False,
        url="https://files.pythonhosted.org/packages/b3/8a/ff81db824035b068f01a82b2e7b1353fdfc6f0a7536791ba0b1a2f9cd4ae/cobra-0.6.1-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.6.2",
        sha256="0b3bdebc55741d4e14e5727ea6e9aa79d6090f7f8264baa31defad5b996692a7",
        expand=False,
        url="https://files.pythonhosted.org/packages/71/d4/23ea187c439c400def7e67f0e980cf0ffb58b3cbb2fe65054800710efd4e/cobra-0.6.2-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.7.0",
        sha256="26779c125b31f6d6adc7c90d58fa480bc5b2751357f64f4ed371a822832f4a0a",
        expand=False,
        url="https://files.pythonhosted.org/packages/39/42/694bfe8bb2bb3cc483253eb9f567617a5b1230af4024530ab15123a4e66b/cobra-0.7.0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.8.0",
        sha256="df8b29c7fe001139f1531565772926046d5d4b2481d9543d229c5c6ad2cbf677",
        expand=False,
        url="https://files.pythonhosted.org/packages/f4/5b/b10101cf3bf82e7cba40c6bec2015f04430fcea2b0375fb2ad3f600bdd35/cobra-0.8.0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.8.1",
        sha256="ada1c212acf55bcc5891ae44b2de92d62815f27dbda77a6a8a1752692bbf9016",
        expand=False,
        url="https://files.pythonhosted.org/packages/7a/b5/d3e9bba33af9a9c1f49212402be71672009c7bb0d2065e48deeb97f992cc/cobra-0.8.1-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.8.2",
        sha256="4caeab549779ff8c197075359221ecd86ebe7a720bf607670b04cd007ca00668",
        expand=False,
        url="https://files.pythonhosted.org/packages/fb/db/fddcf2ca78f1356c641ef20a28da0c0c5ad8dfe2a59311523a49bcdc9cd0/cobra-0.8.2-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.9.0",
        sha256="97f5263922962849262e1b9fd0251b401534a235024c55df336c47ffc2593ae3",
        expand=False,
        url="https://files.pythonhosted.org/packages/ab/5f/619e5f949066afa1749de60617393090b3b00698ece28e5f9d8166192d4c/cobra-0.9.0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "0.9.1",
        sha256="7b14da3f4c14879b5a3f01fa248e9c00f6e16e3c4770d5f0bae1d00b3301df13",
        expand=False,
        url="https://files.pythonhosted.org/packages/21/82/4c3779830ae38563858ee3a99f4dc3190f8f66eb543832ec34ecba04abe0/cobra-0.9.1-cp36-cp36m-manylinux1_x86_64.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-appdirs", type=("build", "run"))
    depends_on("py-depinfo", type=("build", "run"))
    depends_on("py-diskcache", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
    depends_on("py-httpx", type=("build", "run"))
    depends_on("py-importlib-resources", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-optlang", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pydantic@1", type=("build", "run"))
    depends_on("py-python-libsbml", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-swiglpk", type=("build", "run"))


# {'six': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1', '0.19.0', '0.20.0', '0.21.0', '0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], 'future': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1', '0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0', '0.29.1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], 'swiglpk': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1', '0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0', '0.29.1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], 'ruamel.yaml(<0.15)': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], 'numpy(>=1.6)': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], 'pandas(>=0.17.0)': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], 'optlang(>=1.2.5)': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.9.1'], 'tabulate': ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "array;extra=='all'": ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1'], "sbml;extra=='all'": ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1'], "scipy;extra=='array'": ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1', '0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0'], "python-libsbml;extra=='sbml'": ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "lxml;extra=='sbml'": ['0.10.0', '0.10.0a1', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], 'numpy(>=1.13)': ['0.11.3', '0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1'], 'depinfo': ['0.12.0', '0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1', '0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1'], 'optlang(>=1.4.2)': ['0.12.1', '0.13.0', '0.13.1', '0.13.2', '0.13.3', '0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1'], 'ruamel.yaml(>=0.15)': ['0.13.4', '0.14.0', '0.14.1', '0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4'], "python-libsbml;extra=='all'": ['0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "lxml;extra=='all'": ['0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "scipy;extra=='all'": ['0.14.2', '0.15.0', '0.15.1', '0.15.1a0', '0.15.2', '0.15.3', '0.15.4', '0.16.0', '0.17.0', '0.17.1', '0.18.1'], 'python-libsbml-experimental(>=5.17.2)': ['0.15.0', '0.15.1', '0.15.1a0'], 'python-libsbml-experimental(==5.17.2)': ['0.15.2'], 'python-libsbml-experimental(>=5.18.0)': ['0.15.3'], 'python-libsbml-experimental(==5.18.0)': ['0.15.4', '0.16.0', '0.17.0', '0.17.1'], 'ruamel.yaml(>=0.16)': ['0.16.0', '0.17.0', '0.17.1', '0.18.1'], 'python-libsbml-experimental(==5.18.1)': ['0.18.1', '0.19.0'], 'importlib-resources': ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'numpy(~=1.13)': ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0'], 'optlang(~=1.4)': ['0.19.0'], 'pandas(~=1.0)': ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'ruamel.yaml(~=0.16)': ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], "black;extra=='development'": ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0'], "bumpversion;extra=='development'": ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0'], "isort;extra=='development'": ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0'], "tox;extra=='development'": ['0.19.0', '0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3', '0.27.0', '0.28.0', '0.29.0'], 'appdirs(~=1.4)': ['0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'diskcache(~=5.0)': ['0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'httpx(~=0.14)': ['0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2'], 'optlang(<1.4.6)': ['0.20.0', '0.21.0'], 'pydantic(~=1.6)': ['0.20.0', '0.21.0', '0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'python-libsbml-experimental(==5.18.3)': ['0.20.0'], 'rich(~=6.0)': ['0.20.0', '0.21.0'], 'python-libsbml(==5.19.0)': ['0.21.0', '0.22.0', '0.22.1'], 'optlang(~=1.5)': ['0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'rich(>=8.0)': ['0.22.0', '0.22.1', '0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'depinfo(~=1.7)': ['0.23.0', '0.24.0', '0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'python-libsbml(==5.19.2)': ['0.23.0', '0.24.0'], 'python-libsbml(~=5.19)': ['0.25.0', '0.26.0', '0.26.2', '0.26.3'], 'numpy(<1.24,>=1.13)': ['0.26.2', '0.26.3'], 'httpx(~=0.24)': ['0.26.3'], 'appdirs~=1.4': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'depinfo~=1.7': ['0.27.0'], 'diskcache~=5.0': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'httpx~=0.24': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'numpy>=1.13': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'optlang~=1.5': ['0.27.0', '0.28.0'], 'pandas~=1.0': ['0.27.0'], 'pydantic>=1.6': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'python-libsbml~=5.19': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'rich>=8.0': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'ruamel.yaml~=0.16': ['0.27.0', '0.28.0', '0.29.0', '0.29.1'], 'depinfo~=2.2': ['0.28.0', '0.29.0', '0.29.1'], 'pandas<3.0,>=1.0': ['0.28.0', '0.29.0', '0.29.1'], 'optlang~=1.8': ['0.29.0', '0.29.1'], 'scipy;extra=="array"': ['0.29.1'], 'black;extra=="development"': ['0.29.1'], 'bumpversion;extra=="development"': ['0.29.1'], 'isort;extra=="development"': ['0.29.1'], 'tox;extra=="development"': ['0.29.1'], "Cython(>=0.21);extra=='all'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "matplotlib;extra=='all'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "numpy(>=1.6);extra=='all'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "palettable;extra=='all'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "pandas;extra=='all'": ['0.4.1'], "pymatbridge;extra=='all'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "scipy(>=11.0);extra=='all'": ['0.4.1'], "numpy(>=1.6);extra=='array'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "scipy(>=11.0);extra=='array'": ['0.4.1'], "matplotlib;extra=='display'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "palettable;extra=='display'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "pandas;extra=='display'": ['0.4.1'], "pymatbridge;extra=='matlab'": ['0.4.1', '0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.9.1'], "pandas(>=0.17.0);extra=='all'": ['0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "scipy(>=0.11.0);extra=='all'": ['0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0'], "scipy(>=0.11.0);extra=='array'": ['0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1', '0.6.0', '0.6.0a1', '0.6.0a2', '0.6.0a4', '0.6.0a5', '0.6.0a6', '0.6.0a7', '0.6.1', '0.6.2', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '0.9.0'], "pandas(>=0.17.0);extra=='display'": ['0.4.2b1', '0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "tabulate;extra=='all'": ['0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "tabulate;extra=='display'": ['0.5.0b2', '0.5.10', '0.5.11', '0.5.1b1', '0.5.1b2', '0.5.1b3', '0.5.2', '0.5.2b3', '0.5.3.post3', '0.5.4', '0.5.6', '0.5.6b2', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "pytest;extra=='all'": ['0.5.10', '0.5.11', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "pytest-benchmark;extra=='all'": ['0.5.10', '0.5.11', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "pytest;extra=='test'": ['0.5.10', '0.5.11', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], "pytest-benchmark;extra=='test'": ['0.5.10', '0.5.11', '0.5.7', '0.5.8', '0.5.9', '0.5.9b1'], 'optlang(>=1.1.5)': ['0.6.0', '0.6.1', '0.6.2', '0.7.0'], 'ruamel.yaml': ['0.6.0', '0.6.1'], 'optlang': ['0.6.0a1', '0.6.0a2', '0.6.0a4'], 'optlang(>=1.1.4)': ['0.6.0a5', '0.6.0a6', '0.6.0a7'], 'optlang(>=1.2.1)': ['0.8.0', '0.8.1', '0.8.2', '0.9.0'], "scipy(==0.19.1);extra=='all'": ['0.9.1'], "scipy(==0.19.1);extra=='array'": ['0.9.1']}
