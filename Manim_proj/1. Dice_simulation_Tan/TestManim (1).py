from manim import *
import random

class Dice(Scene):
    def construct(self):
        numbers = VGroup() # nhóm lại thành vector
        for x in range(10):
            num = Integer() # tạo ra 1 số thực
            numbers.add(num)

        def randomize_numbers(numbers): #tạo và tô màu cho số(dòng 1)
            for num in numbers:
                value = random.randint(1, 6)
                num.set_value(value)
                num.set_color(GREEN)

        randomize_numbers(numbers)

        numbers.set(width=0.3)
        numbers.arrange(RIGHT, buff=0.2)
        numbers.to_edge(ORIGIN)

        for k in range(10):
            self.play(UpdateFromFunc(numbers, randomize_numbers)) #cập nhật giá trị 
            self.wait()
            box = SurroundingRectangle(numbers)
            self.play(Create(box))
            self.play(FadeOut(box), FadeOut(numbers))
        self.wait()

# Create dices 
def create_dice(count: int,size: float,radius: float,color_dice: color = WHITE, color_circle: color = BLACK,) -> VGroup:
    dice = VGroup()
    dice_shape = RoundedRectangle(
        width=size,
        height=size,
        corner_radius=radius,
        color=BLACK,
        fill_color=color_dice,
        fill_opacity=1,
    )
    dot_dice = [
        Circle(
            radius=size / 12, stroke_width=0, fill_color=color_circle, fill_opacity=1
        )
        for _ in range(count)
    ]
    dice.add(dice_shape, *dot_dice)

    match count:
        case 1:
            dot_dice[0].move_to(dice_shape.get_center())
        case 2:
            dot_dice[0].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
        case 3:
            dot_dice[0].move_to(dice_shape.get_center())
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
        case 4:
            dot_dice[0].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_top()
                )
            )
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[3].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_bottom()
                )
            )
        case 5:
            dot_dice[0].move_to(dice_shape.get_center())
            dot_dice[1].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_top()
                )
            )
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
            dot_dice[3].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[4].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_bottom()
                )
            )
        case _:
            dot_dice[0].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_top()
                )
            )
            dot_dice[1].move_to(0.5 * (dice_shape.get_center() + dice_shape.get_left()))
            dot_dice[2].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_left()
                    + dice_shape.get_bottom()
                )
            )
            dot_dice[3].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_top()
                )
            )
            dot_dice[4].move_to(
                0.5 * (dice_shape.get_center() + dice_shape.get_right())
            )
            dot_dice[5].move_to(
                0.5
                * (
                    dice_shape.get_center()
                    + dice_shape.get_right()
                    + dice_shape.get_bottom()
                )
            )

    return dice



def get_data_1(self):
    w = 0.2
    row1 = (
        VGroup(
            *[
                create_dice(1, 0.75, 0.2).set(width=w)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .to_edge(UL, buff=0.25)
    )
    row2 = (
        VGroup(
            *[
                create_dice(2, 0.75, 0.2).set(width=w)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(row1, DOWN, buff=0.25)
    )
    row3 = (
        VGroup(
            *[
                create_dice(3, 0.75, 0.2).set(width=w)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(row2, DOWN, buff=0.25)
    )
    row4 = (
        VGroup(
            *[
                create_dice(4, 0.75, 0.2).set(width=w)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(row3, DOWN, buff=0.25)
    )
    row5 = (
        VGroup(
            *[
                create_dice(5, 0.75, 0.2).set(width=w)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(row4, DOWN, buff=0.25)
    )
    row6 = (
        VGroup(
            *[
                create_dice(6, 0.75, 0.2).set(width=w)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(row5, DOWN, buff=0.25)
    )

    result = VGroup(*row1, *row2, *row3, *row4, *row5, *row6)

    return result

class CentralLimitTheorem(Scene):
    def construct(self):
        data = get_data_1(self)
        axes = (
            Axes(x_range=[0, 60, 5], y_range=[0, 2.5], x_length=13, y_length=4)
            .to_edge(DL)
            .shift(UP * 0.2)
        )

        #labels = axes.get_axis_labels(x_label="\\hat{p}", y_label="")

        x_axis_nums = VGroup()
        for i in range(13):
            num = (
                MathTex(str(i * 5))
                .scale(0.6)
                .next_to(axes.x_axis.n2p(i*5), DOWN, buff=0.1)
            )
            x_axis_nums.add(num)
        #axes_group = Group(axes, labels, x_axis_nums)
        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT * 0.6)
        total_counter = (
            Tex("Sum of Averages: ")
            .scale(0.6)
            .next_to(sample_counter, DOWN, aligned_edge=LEFT, buff=0.4)
        )
        average_counter = (
            MathTex("Average \\ \\hat{p}:  ")
            .scale(0.6)
            .next_to(total_counter, DOWN, aligned_edge=LEFT, buff=0.4)
        )

        self.play(
            LaggedStart(
                Create(data),
                Write(VGroup(sample_counter, total_counter, average_counter)),
                Create(axes),
                Write(x_axis_nums),
                run_time=4,
                lag_ratio=1,
            )
        )
        self.wait()

        data = get_data_1(self)
        sample_count = 10
        possible_outcomes = sample_count + 1 #từ 0 đến sample count
        counter_num = 0
        counter_number = (
            Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        )
        counter_number.add_updater(lambda m: m.set_value(counter_num)) #cập nhật

        total_sum = 0
        total_number = (
            Integer(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        )
        total_number.add_updater(lambda m: m.set_value(total_sum))

        average = 0
        average_num = (
            DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        )
        average_num.add_updater(lambda m: m.set_value(average))

        self.add(counter_number, total_number, average_num)

        sums = [0] * possible_outcomes  # This creates an array for possible totals /10

        for s in range(5):
            # THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0, 60), k=sample_count) 

            # THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            sample_results = VGroup()
            boxes = VGroup()
            for i, res in enumerate(a):
                res = data[a[i]] #retrieves the visual element corresponding to the sampled value from data
                box = SurroundingRectangle(res)
                sample_results.add(res)
                boxes.add(box)

            moved_result = sample_results.copy() #This copy will be used for animations, allowing the original sample_results to remain unchanged

            self.play(Create(boxes))
            self.play(
                moved_result.animate.arrange(RIGHT * 0.3, buff=0).to_edge(UP),
                FadeOut(boxes),
            )

            # THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i, value in enumerate(a):
                if value < 10:
                    a[i] = 1
                elif value < 20:
                    a[i] = 2
                elif value < 30:
                    a[i] = 3
                elif value < 40:
                    a[i] = 4
                elif value < 50:
                    a[i] = 5
                else:
                    a[i] = 6
                
            prop = DecimalNumber(num_decimal_places=1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set(height=0.2)
            prop.next_to(moved_result, RIGHT, buff=0.3)

            axes_box = SurroundingRectangle(
                moved_result,
                stroke_color=WHITE,
                stroke_width=0.2,
                fill_color=BLUE,
                fill_opacity=0.8,
                buff=0.1,
            )
            stack_in_axes = VGroup(axes_box, moved_result)
            self.play(DrawBorderThenFill(axes_box))
            self.play(Write(prop))

            counter_num += 1

            total_sum += tot / sample_count

            average = (total_sum) / (counter_num)

            self.play(
                stack_in_axes.animate.next_to(x_axis_nums[int(tot / 5)], UP, buff=0)
                .set(width=0.77)
                .shift(UP * sums[int(tot / 5)]),
                FadeOut(prop),
            )
            sums[int(tot / 5)] += stack_in_axes.get_height()

        self.wait()

        for s in range(45):
            # THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0, 60), k=sample_count)

            # THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            sample_results = VGroup()
            boxes = VGroup()
            for i, res in enumerate(a):
                res = data[a[i]]
                box = SurroundingRectangle(res)
                sample_results.add(res)
                boxes.add(box)

            moved_result = sample_results.copy()

            self.play(Create(boxes), run_time=0.1)
            self.play(
                moved_result.animate.arrange(RIGHT * 0.3, buff=0).to_edge(UP),
                FadeOut(boxes),
                run_time=0.1,
            )

            # THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i, value in enumerate(a):
                if value < 10:
                    a[i] = 1
                elif value < 20:
                    a[i] = 2
                elif value < 30:
                    a[i] = 3
                elif value < 40:
                    a[i] = 4
                elif value < 50:
                    a[i] = 5
                else:
                    a[i] = 6

            prop = DecimalNumber(num_decimal_places=1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set(height=0.2)
            prop.next_to(moved_result, RIGHT, buff=0.3)

            axes_box = SurroundingRectangle(
                moved_result,
                stroke_color=WHITE,
                stroke_width=0.2,
                fill_color=BLUE,
                fill_opacity=0.8,
                buff=0.1,
            )
            stack_in_axes = VGroup(axes_box, moved_result)
            self.add(axes_box, prop)
            counter_num += 1
            total_sum += tot / sample_count
            average = (total_sum) / (counter_num)

            self.play(
                stack_in_axes.animate.next_to(x_axis_nums[int(tot / 5)], UP, buff=0)
                .set(width=0.77)
                .shift(UP * sums[int(tot / 5)]),
                FadeOut(prop),
                run_time=0.3,
            )
            sums[int(tot / 5)] += stack_in_axes.get_height()
        self.wait()
