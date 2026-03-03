# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPy3dmol(PythonPackage):
    """An IPython interface for embedding 3Dmol.js views in Jupyter notebooks"""

    homepage = "https://3dmol.org"
    pypi = "py3Dmol/py3Dmol-2.4.2-py2.py3-none-any.whl"

    version(
        "0.5.0",
        sha256="78bf782d7f4c700a0c63dad18b5ad00d9d4ea1fe0ed85296dd7fecec9b9412c5",
        expand=False,
        url="https://files.pythonhosted.org/packages/f4/a9/ce9f532362c3f1d9504e335483520d858f719a3380fccabe96362139161a/py3Dmol-0.5.0-py2.py3-none-any.whl",
    )
    version(
        "0.5.1",
        sha256="864ce8a81685ffc229cae173f472233e9fdfeaa7ce4941fded94d3c4a1b5c941",
        expand=False,
        url="https://files.pythonhosted.org/packages/1d/d0/f01675d75365e51ee6c3f36d2964ab8d38e86ebef948b511247449641abb/py3Dmol-0.5.1-py2.py3-none-any.whl",
    )
    version(
        "0.5.2",
        sha256="fe2fda4e1dc03fe7617135a338dac6d0a832f2922b205444b591d775bd211867",
        expand=False,
        url="https://files.pythonhosted.org/packages/15/0f/1eaf6ce39fd69c54915b258d00d304b987e272ffa6ff092ba68ac244d01e/py3Dmol-0.5.2-py2.py3-none-any.whl",
    )
    version(
        "0.5.3",
        sha256="260a8a970ba897ee6b6c60559291988fa79ef7729cf81b658df32f24ca9e8fdc",
        expand=False,
        url="https://files.pythonhosted.org/packages/eb/d9/f0a3018a2826b364f752b0ee334e9afe1857f1da5ef05e4987df0eb8c7dc/py3Dmol-0.5.3-py2.py3-none-any.whl",
    )
    version(
        "0.5.4",
        sha256="a73f70e09e8006666ecfb93398672c1a1554675be6717b9b9192fd74067c578c",
        expand=False,
        url="https://files.pythonhosted.org/packages/2c/79/ba22beb8d307149f385f41387d7260c6bf3b75be861ab693f7db07c85916/py3Dmol-0.5.4-py2.py3-none-any.whl",
    )
    version(
        "0.6.0",
        sha256="145f95d7be5abc104619e57348e908b5a5fdb1b9131066acef6349cb762efe82",
        expand=False,
        url="https://files.pythonhosted.org/packages/05/9f/ecd499ab4de5c64ac6a0173b162910f3bcb91d0da475c7666f60f4c4480c/py3Dmol-0.6.0-py2.py3-none-any.whl",
    )
    version(
        "0.6.1",
        sha256="fe628f74932bb6ca9fd3f38e8ae80c3083096c5a9416a093b112150dc078facc",
        expand=False,
        url="https://files.pythonhosted.org/packages/1b/bb/59c2092fa6ae3ed836792ad2d806a9b4a36bf71ffff350872eccba82b768/py3Dmol-0.6.1-py2.py3-none-any.whl",
    )
    version(
        "0.6.2",
        sha256="c62b9d7c9aca9118a6548b2beadb8a147452cecf3b7f158e140e56ea098dd9c2",
        expand=False,
        url="https://files.pythonhosted.org/packages/ab/4e/6d6167d7f9ac8dec5be1a49b6868f84c2fdf8d188500bc2a10d4adcd6ae6/py3Dmol-0.6.2-py2.py3-none-any.whl",
    )
    version(
        "0.6.3",
        sha256="23f75dc2e57911f624bd1de3f64d8c54af84a934e111f8578e9cd7710fcdf725",
        expand=False,
        url="https://files.pythonhosted.org/packages/10/39/90b4ad31fd7991862eb69b56cea0aa86d35090ce8d6b282dcf2655c185eb/py3Dmol-0.6.3-py2.py3-none-any.whl",
    )
    version(
        "0.6.4",
        sha256="141824f075437744659ad59aaf41a430bc0211ebf7c3598cc49b24d7cb914d2e",
        expand=False,
        url="https://files.pythonhosted.org/packages/bf/f5/73b1e2844f722ceb558a11e4f3eb760d167b00ca2d3f29e1b028755a382b/py3Dmol-0.6.4-py2.py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="3da84c5a7d0d1257d580d44b00214e823debe6b1397a77ca1b372158db266216",
        expand=False,
        url="https://files.pythonhosted.org/packages/ba/f1/e36dea28d4b655280bb18382f3d452717f2338402a618b6710bf04710cf6/py3Dmol-0.7.0-py2.py3-none-any.whl",
    )
    version("0.7.1", sha256="0368b235d7210912e3582e31d984adc77e546dc3b3320483437a8aa60f89706a")
    version(
        "0.7.2",
        sha256="90d5c72731e8e15757606dd36b3f62d864146cdf6f4be4adf30a1d93cbc35a71",
        expand=False,
        url="https://files.pythonhosted.org/packages/f8/8a/4cf31928a03b13f30e8b00134565990331087145f6e5248fd1bd7dcc2631/py3Dmol-0.7.2-py2.py3-none-any.whl",
    )
    version(
        "0.8.0",
        sha256="19874ba64a5f1a4ccd63f85321742a005de7083f2496610918c0e92497733ce0",
        expand=False,
        url="https://files.pythonhosted.org/packages/da/87/44984bfc8a3014c1386661be4efeeee7d3fe811b79802695100620cedda6/py3Dmol-0.8.0-py2.py3-none-any.whl",
    )
    version(
        "0.8.1",
        sha256="adca0f72fb5a5f24b26aedb4b7a9043dc95020f46703e3f7e1ab92a1539b02da",
        expand=False,
        url="https://files.pythonhosted.org/packages/be/49/351994057806d6076d22b51215d2b18b1e332b646f1fe8719907aa0b12ff/py3Dmol-0.8.1-py2.py3-none-any.whl",
    )
    version(
        "0.9.0",
        sha256="d7bc2251653cc3b25af5ce73d8a7f240b1d335919da4d2987b313d18002a2678",
        expand=False,
        url="https://files.pythonhosted.org/packages/f9/78/812e79e152aeeec09d92c27d802186eb137a653c6b3b102afb7c4c755884/py3Dmol-0.9.0-py2.py3-none-any.whl",
    )
    version(
        "0.9.1",
        sha256="580585ddb6ed056e3be473542c33e2b5f2fd2e434ea74ec600d5613ed52c92d3",
        expand=False,
        url="https://files.pythonhosted.org/packages/dd/19/dd527b0db65e730e20c3d5e5a7efbb7fbbf8d98f9debfb47962c13f479d6/py3Dmol-0.9.1-py2.py3-none-any.whl",
    )
    version(
        "0.9.2",
        sha256="ae361be10d903326e890bb84052bac5e77ed2d3eaadff1135597f3223213d9a3",
        expand=False,
        url="https://files.pythonhosted.org/packages/ea/5e/044713fee4c34fb38abbe231b6a550226ef5f76558ca4080b4aeacaeeda6/py3Dmol-0.9.2-py2.py3-none-any.whl",
    )
    version(
        "1.7.0",
        sha256="ff35bd17ed23a795a06faf13284280504cc8d6860ce916450975a313267ff88f",
        expand=False,
        url="https://files.pythonhosted.org/packages/31/7b/4faef9685527e530328c4549f1dd95799becbd87099986deec3a93484c10/py3Dmol-1.7.0-py2.py3-none-any.whl",
    )
    version(
        "1.8.0",
        sha256="7fa6183056f6890af145e30e99a7b415f43dc3967bd8dd481f4108878722389e",
        expand=False,
        url="https://files.pythonhosted.org/packages/f5/25/6b7324df6c09e096e458e1393fa714eddc726fa2792f3019430f8a2f139e/py3Dmol-1.8.0-py2.py3-none-any.whl",
    )
    version(
        "1.8.1",
        sha256="c4741f1bc2e219024b165e36c3e5c172c0550a3a36b81825d2a9d0eff06cd714",
        expand=False,
        url="https://files.pythonhosted.org/packages/c9/c3/4cabc0b0b32d90e4862a9f77f3e712b21821fcf77facf3422dbd7f2bc438/py3Dmol-1.8.1-py2.py3-none-any.whl",
    )
    version(
        "2.0.0",
        sha256="dd32f79fbe7b2ae052c44d1773979c96d3be1f98845eb02705d373bc8b1b2ea3",
        expand=False,
        url="https://files.pythonhosted.org/packages/dd/b6/0ba143f091b1012676d580ca81b5bdedea9e9a04c47da09addcd636f10e6/py3Dmol-2.0.0-py2.py3-none-any.whl",
    )
    version(
        "2.0.0.post1",
        sha256="fa4cd664ea7f15c0b90af92d92dca75d5d10dc009f86efe5dbf32138200e461b",
        expand=False,
        url="https://files.pythonhosted.org/packages/53/70/ba6f721a6c6dd711ac0fb50d8002c28e48a2114683f0d60cdac4a833511c/py3Dmol-2.0.0.post1-py2.py3-none-any.whl",
    )
    version(
        "2.0.0.post2",
        sha256="508f4569c3fbe9781cd28527ab8d0fa5e80c49ebdf00ad2ba43de6dab25fb381",
        expand=False,
        url="https://files.pythonhosted.org/packages/1a/b7/a6a8b6c2a832b368393b442578cde0909ab214d77238e3c03493174b0ebf/py3Dmol-2.0.0.post2-py2.py3-none-any.whl",
    )
    version(
        "2.0.1",
        sha256="a6d5ea0b2bda7a60f2da5bfa145f48baf4c5cf315e9a095c937a2b81b1c5227d",
        expand=False,
        url="https://files.pythonhosted.org/packages/2a/1f/f5276d31ae6b248692fc977ae6755414c843462b4d5641484423487048a8/py3Dmol-2.0.1-py2.py3-none-any.whl",
    )
    version(
        "2.0.1.post1",
        sha256="809151c25f8367d20eb075757316f3956b79b7aeda487ac20f9053f7b41a80ff",
        expand=False,
        url="https://files.pythonhosted.org/packages/a5/d0/9a5aeb9d6fd9dc73055ec62641d8cd0d2c21a9ec819ef7b04cecac3267e9/py3Dmol-2.0.1.post1-py2.py3-none-any.whl",
    )
    version(
        "2.0.3",
        sha256="09f56d9942502ba8a6cc96c80e7506f41c5e53f801880df4610a2bc29fd62523",
        expand=False,
        url="https://files.pythonhosted.org/packages/47/69/b295c4c0f7c9e9ddbb3f94577c0b15ddedb4dbbf08a451bdac5d0f5d4831/py3Dmol-2.0.3-py2.py3-none-any.whl",
    )
    version(
        "2.0.4",
        sha256="356a3a9fee9c48be9b010228790ce394bd4d90d3fd47448964fcbfa6dc5e0a84",
        expand=False,
        url="https://files.pythonhosted.org/packages/b5/3d/052e5932ef95624e118b886feb58a9c60595e89da74515604933b6b0e6a5/py3Dmol-2.0.4-py2.py3-none-any.whl",
    )
    version(
        "2.1.0",
        sha256="1093919800d66b229c0bb8d247869ccc26cbb4674644988ba2f4f3658f21ff0e",
        expand=False,
        url="https://files.pythonhosted.org/packages/d0/06/8b41d1dd0ac73d653c76f68563a8a12f44de4de80d92807f9d35c2cbc33e/py3Dmol-2.1.0-py2.py3-none-any.whl",
    )
    version(
        "2.2.0",
        sha256="d5d8d390d95fdd0cc2b190f6b8204f0e489aef656cad75b85630196572803151",
        expand=False,
        url="https://files.pythonhosted.org/packages/02/08/860a7d437f201f407e0373ba0faaf12bc2bc778355eb631e0a0ea22c5bb7/py3Dmol-2.2.0-py2.py3-none-any.whl",
    )
    version(
        "2.2.1",
        sha256="0637bb977dc36b513e632b178e7bc59ce3daf9295d409eba002de099e6408836",
        expand=False,
        url="https://files.pythonhosted.org/packages/6c/ab/acecba7254222d3deca88d8a6b8086c469cdc3a8e376ed21f75e15d4f5c3/py3Dmol-2.2.1-py2.py3-none-any.whl",
    )
    version(
        "2.3.0",
        sha256="d94df1edebbe40ae24512735008fac46c511c27958afa7f649472034af3c91f7",
        expand=False,
        url="https://files.pythonhosted.org/packages/56/72/200c6f40642bd31db2f8da07b4bfe0d84cb513af8c2dfca953d388e9e04d/py3Dmol-2.3.0-py2.py3-none-any.whl",
    )
    version(
        "2.4.0",
        sha256="e7d27ffdf9326850e4c6dac55ec047ce023ffaf87d8032278982a4d3d78d3973",
        expand=False,
        url="https://files.pythonhosted.org/packages/63/a6/ccb9b29ad5aa0857b140426a0429ed363e5856513303ddcb233b30906bb1/py3Dmol-2.4.0-py2.py3-none-any.whl",
    )
    version(
        "2.4.1",
        sha256="5e56c79703a183b89cf9c5659a01f6cd7e9836a0919d72e2c43f96f45c9bafd8",
        expand=False,
        url="https://files.pythonhosted.org/packages/b1/41/d39f2587db5c497a83f68315f4b78b450b59f5189e1c9c106d1ee7c85935/py3Dmol-2.4.1-py2.py3-none-any.whl",
    )
    version(
        "2.4.2",
        sha256="bec23d9a015d692279a5f7d4db92803e4e82ba3bdcc1434a5b6a2be98a347856",
        expand=False,
        url="https://files.pythonhosted.org/packages/04/20/923885064f4e4d4392eb2be798532d91b315f9e60ef44f49f4800ba3c57a/py3Dmol-2.4.2-py2.py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-jupyter", type=("build", "run"))


# {'idisplay': ['0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.7.0', '0.7.2', '0.8.0'], 'jupyter': ['0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.7.0', '0.7.2', '0.8.0'], "IPython;extra=='ipython'": ['0.8.1', '0.9.0', '0.9.1', '0.9.2', '1.7.0', '1.8.0', '1.8.1', '2.0.0', '2.0.0.post1', '2.0.0.post2', '2.0.1', '2.0.1.post1', '2.0.3', '2.0.4', '2.1.0', '2.2.0', '2.2.1', '2.3.0', '2.4.0', '2.4.1', '2.4.2']}
