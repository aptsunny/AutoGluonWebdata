```markdown
# Darts 搜索空间设计
CNN(
  (stem): Sequential(
    (0): Conv2d(3, 48, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
    (1): BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  )
  (cells): ModuleList(
    (0): Cell(
      (preproc0): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(48, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(48, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (normal_n2_p0)
            (1): _key (normal_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (normal_n3_p0)
            (1): _key (normal_n3_p1)
            (2): _key (normal_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (normal_n4_p0)
            (1): _key (normal_n4_p1)
            (2): _key (normal_n4_p2)
            (3): _key (normal_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (normal_n5_p0)
            (1): _key (normal_n5_p1)
            (2): _key (normal_n5_p2)
            (3): _key (normal_n5_p3)
            (4): _key (normal_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n5_switch)
        )
      )
    )
    (1): Cell(
      (preproc0): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(48, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(64, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (normal_n2_p0)
            (1): _key (normal_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (normal_n3_p0)
            (1): _key (normal_n3_p1)
            (2): _key (normal_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (normal_n4_p0)
            (1): _key (normal_n4_p1)
            (2): _key (normal_n4_p2)
            (3): _key (normal_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (normal_n5_p0)
            (1): _key (normal_n5_p1)
            (2): _key (normal_n5_p2)
            (3): _key (normal_n5_p3)
            (4): _key (normal_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n5_switch)
        )
      )
    )
    (2): Cell(
      (preproc0): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(64, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(64, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (reduce_n2_p0)
            (1): _key (reduce_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (reduce_n3_p0)
            (1): _key (reduce_n3_p1)
            (2): _key (reduce_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (reduce_n4_p0)
            (1): _key (reduce_n4_p1)
            (2): _key (reduce_n4_p2)
            (3): _key (reduce_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (reduce_n5_p0)
            (1): _key (reduce_n5_p1)
            (2): _key (reduce_n5_p2)
            (3): _key (reduce_n5_p3)
            (4): _key (reduce_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n5_switch)
        )
      )
    )
    (3): Cell(
      (preproc0): FactorizedReduce(
        (relu): ReLU()
        (conv1): Conv2d(64, 16, kernel_size=(1, 1), stride=(2, 2), bias=False)
        (conv2): Conv2d(64, 16, kernel_size=(1, 1), stride=(2, 2), bias=False)
        (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(128, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (normal_n2_p0)
            (1): _key (normal_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (normal_n3_p0)
            (1): _key (normal_n3_p1)
            (2): _key (normal_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (normal_n4_p0)
            (1): _key (normal_n4_p1)
            (2): _key (normal_n4_p2)
            (3): _key (normal_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (normal_n5_p0)
            (1): _key (normal_n5_p1)
            (2): _key (normal_n5_p2)
            (3): _key (normal_n5_p3)
            (4): _key (normal_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n5_switch)
        )
      )
    )
    (4): Cell(
      (preproc0): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(128, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(128, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (normal_n2_p0)
            (1): _key (normal_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (normal_n3_p0)
            (1): _key (normal_n3_p1)
            (2): _key (normal_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (normal_n4_p0)
            (1): _key (normal_n4_p1)
            (2): _key (normal_n4_p2)
            (3): _key (normal_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (normal_n5_p0)
            (1): _key (normal_n5_p1)
            (2): _key (normal_n5_p2)
            (3): _key (normal_n5_p3)
            (4): _key (normal_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n5_switch)
        )
      )
    )
    (5): Cell(
      (preproc0): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (reduce_n2_p0)
            (1): _key (reduce_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (reduce_n3_p0)
            (1): _key (reduce_n3_p1)
            (2): _key (reduce_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (reduce_n4_p0)
            (1): _key (reduce_n4_p1)
            (2): _key (reduce_n4_p2)
            (3): _key (reduce_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (reduce_n5_p0)
            (1): _key (reduce_n5_p1)
            (2): _key (reduce_n5_p2)
            (3): _key (reduce_n5_p3)
            (4): _key (reduce_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (reduce_n5_switch)
        )
      )
    )
    (6): Cell(
      (preproc0): FactorizedReduce(
        (relu): ReLU()
        (conv1): Conv2d(128, 32, kernel_size=(1, 1), stride=(2, 2), bias=False)
        (conv2): Conv2d(128, 32, kernel_size=(1, 1), stride=(2, 2), bias=False)
        (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (normal_n2_p0)
            (1): _key (normal_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (normal_n3_p0)
            (1): _key (normal_n3_p1)
            (2): _key (normal_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (normal_n4_p0)
            (1): _key (normal_n4_p1)
            (2): _key (normal_n4_p2)
            (3): _key (normal_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (normal_n5_p0)
            (1): _key (normal_n5_p1)
            (2): _key (normal_n5_p2)
            (3): _key (normal_n5_p3)
            (4): _key (normal_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n5_switch)
        )
      )
    )
    (7): Cell(
      (preproc0): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (preproc1): StdConv(
        (net): Sequential(
          (0): ReLU()
          (1): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
        )
      )
      (mutable_ops): ModuleList(
        (0): Node(
          (ops): ModuleList(
            (0): _key (normal_n2_p0)
            (1): _key (normal_n2_p1)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n2_switch)
        )
        (1): Node(
          (ops): ModuleList(
            (0): _key (normal_n3_p0)
            (1): _key (normal_n3_p1)
            (2): _key (normal_n3_p2)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n3_switch)
        )
        (2): Node(
          (ops): ModuleList(
            (0): _key (normal_n4_p0)
            (1): _key (normal_n4_p1)
            (2): _key (normal_n4_p2)
            (3): _key (normal_n4_p3)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n4_switch)
        )
        (3): Node(
          (ops): ModuleList(
            (0): _key (normal_n5_p0)
            (1): _key (normal_n5_p1)
            (2): _key (normal_n5_p2)
            (3): _key (normal_n5_p3)
            (4): _key (normal_n5_p4)
          )
          (drop_path): DropPath()
          (input_switch): _key (normal_n5_switch)
        )
      )
    )
  )
  (gap): AdaptiveAvgPool2d(output_size=1)
  (linear): Linear(in_features=256, out_features=10, bias=True)
)
```

