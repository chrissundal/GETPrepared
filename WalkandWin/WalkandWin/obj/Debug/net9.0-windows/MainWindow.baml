   M S B A M L   `   `   `  ����E  AWalkandWin, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null'clr-namespace:WalkandWin
WalkandWin  5   	       WalkandWin.MainWindow   5   	   W SPresentationCore, Version=9.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=9.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=9.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=9.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=9.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   *localclr-namespace:WalkandWin     5   	     � Title$  Walk and Win��5   	   $	��450��6   $	��800��6+   ���#f0f0f0 � Icon$+ %pack://application:,,,/Icons/walk.png��5	   	    � 	Resources 5
       �� 
TargetType �� Property �� Value��%�  '��       '�� )    �� 5   
   " ��6   .�5      ��  � ��$ 16(�6)   �� 5       � ��$ 10q�6(   �� 5       � ��$ 10q�6'   �� 5       � �� �#007ACC6+   �� 5       � ��
 �����6+   �� 5       � ��
 ���� 6,   �� 5       � ��$ 0q�60   5      �� 5   
   " ��6   .�5      ��  � ��$ 24(�6)   �� 5       � ��$ 10q�6'   5      5      .��5      �  � RowDefinitions 5   
   �� 5      $
��Auto �6   �� 5      $��* �6   �� 5      $
��Auto �6   .+�5   
   �� -   5        $/��)/bin/Debug/net9.0-windows/Images/gear.png��5      $��30��6C   $��30��6N   $
��Left=�5       $	��Top=�6+   $��10q�5!      6   �� 5"   
   -   5        $��Message��5"      $��Center=�6#   $	��Top=�6@   $��0��6X   $��10q�6e   $
��Bold"�6q   �� 5#   
    �� Orientation$ Vertical=�6   $��Center=�6,   $��Center=�6I   $��1��6d   .+�5$      �� -   5        $��CountdownText��5$      $��Center=�6-   $��48(�6J   $
��Bold"�6X   $��20q�6j   �� 5%      $ 
Horizontal=�6   $��Center=�62   .+�5&      �� -   5        $��
DoneButton��5&      $
��Done��6+   $	��100��6:   $��50��6F   $y�	Collapsed=�6k   5'      5(      �� 5)   
   -   5        $��
PointsText��5)      $��Center=�6&   $��Bottom=�6C   $��2��6^   $��50q�6k   $
��Bold"�6w   �� 5*   
   -   5        $��StatusMessage��5*      $��Center=�6)   $��Bottom=�6F   $��3��6a   5+      5,      